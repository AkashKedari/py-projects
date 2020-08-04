import datetime as dt
import matplotlib.pyplot as plt
from matplotlib import style
import mplfinance as mpf
import matplotlib.dates as mdates
import pandas as pd
import pandas_datareader.data as web

style.use('ggplot')

stock=input("Enter the stock ticker symbol:  ")
print(stock)
startyear = int(input("Please enter a start year:  "))
startmonth = int(input("Please enter a start month:  "))
startday = int(input("Please enter a start day:  "))

start = dt.datetime(startyear,startmonth,startday)
now = dt.datetime.now()

df = web.DataReader(stock,'yahoo',start,now)

# Convert data to a csv file
# df.to_csv('TSLA.csv')

# df = pd.read_csv('TSLA.csv', parse_dates = True, index_col=0)

# only printing open and high coloums
# print(df[['Open','High']].head())

# plotting the dataframe, can select specific items to show
# df ['Adj Close'].plot()
# plt.show()

# creating new category in dataframe called '100ma'
# df['100ma'] = df['Adj Close'].rolling(window=100, min_periods=0).mean()

# Resample the df
df_ohlc = df['Adj Close'].resample('10D').ohlc()

# using mpf  to plot a candlestick graph
mpf.plot(df_ohlc, type='candle',style='yahoo')


# ax1 = plt.subplot2grid((6,1),(0,0), rowspan=5 , colspan=1)
# ax2 = plt.subplot2grid((6,1),(5,0), rowspan=1 , colspan=1, sharex=ax1)
# ax1.plot(df.index, df['Adj Close'])
# ax1.plot(df.index, df['100ma'])
# ax2.bar(df.index, df['Volume'])
# plt.show()
