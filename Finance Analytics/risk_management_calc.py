import pandas as pd
import numpy as np
import yfinance as pf
import datetime as dt
from pandas_datareader import data as pdr
import statistics
import time
import matplotlib.pyplot as plt

# Y-finance API workaround
# yf.pdr_override()
now = dt.datetime.now()
start = dt.datetime(2020,1,1)

# Average gain %
AvgGain = 15
# Average loss %
AvgLoss = 5
# Simple moving averages
smaUsed = [50,200]
# Exponential moving averages used
emaUsed = [21]

# User enters stock ticker
stock = input("Enter the stock ticker symbol (enter 'quit' to stop):  ")
print (stock)

# Loop keeps going until user enters "quit"
while stock != "quit":
    # Get stock information
    df = pdr.get_data_yahoo(stock,start,now)
    close = df['Adj Close'][-1]

    # Average loss. Initial stoploss less than max loss.
    maxStop = close*((100-AvgLoss)/100)

    # Average gain. Target Risk
    Target1R = round(close*((100+ AvgGain)/100),2)
    Target2R = round(close*((100+(2*AvgGain))/100),2)
    Target3R = round(close*((100+(3*AvgGain))/100),2)

    # Buys are close to key moving averages. Low risk entry.
    for x in smaUsed:
        sma = x
        df["SMA_"+str(sma)]=round(df.iloc[:,4].rolling(window=sma).mean(),2)
    for x in emaUsed:
        ema = x
        df['EMA_'+str(ema)] = round(df.iloc[:,4].ewm(span=ema,adjust=False).mean(),2)


    # Get most recent values for the sma/ema
    sma50=round(df["SMA_50"][-1],2)
    sma200=round(df["SMA_200"][-1],2)
    ema21=round(df["EMA_21"][-1],2)
    # Low of the previous 5 days
    low5 = round(min(df["Low"].tail(5)),2)

    # Calculate percentages from each smas/ema
    # Percentage from 50 sma
    pf50 = round(((close/sma50)-1)*100,2)
    check50 = df["SMA_50"][-1] > maxStop

    pf200 = round(((close/sma200)-1)*100,2)
    # Checking if the check sma 200 is greater than 100% from that sma.
    # if it is, then stock is in danger zone.
    check200 = ((close/df["SMA_200"][-1])-1)*100 > 100

    pf21 = round(((close/ema21)-1)*100,2)
    # Checking how far stock is above the 21 ema
    check21 = df["EMA_21"][-1] > maxStop

    pfL = round(((close/low5)-1)*100,2)
    # Checks if the low 5 is greater than the maxStop
    checkL = pfL > maxStop

    print()
    print("Current Stock: "+stock+" Price: "+str(round(close,2)))
    print("21 EMA: "+str(ema21)+" | 50 SMA: "+str(sma50)+" | 200 SMA: "+str(sma200)+" | 5 Day Low: "+str(low5))
    print("------------------------------------------------------")
    print ("Max Stop: "+str(round(maxStop,2)))
    print()
    print("Price Targets: ")
    print("1R: "+str(Target1R))
    print("2R: "+str(Target2R))
    print("3R: "+str(Target3R))
    print()
    print("From 5 day low "+str(pfL)+"% -Within Max Stop: "+str(checkL))
    print("From 21 Day EMA "+str(pf21)+"% -Within Max Stop: "+str(check21))
    print("From 50 day SMA "+str(pf50)+"% -Within Max Stop: "+str(check50))
    print("From 200 day SMA "+str(pf200)+"% -Within Max Stop: "+str(check200))
    print()
    print()

    # Input another stock
    stock = input("Enter the stock ticker symbol (enter 'quit' to stop):  ")
