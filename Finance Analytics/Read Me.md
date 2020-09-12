# python_finance: 

This is a simple program that will take OHLC information and streamline it using the .resample() function. 
The information is going to be the adjusted closed values. Matplotlib finance is going to be used to display a candlestick graph of the data. 

# stock_history: 

This is a program that is going to get information of your seleccted ticker. This will calculate EMA using different time dates. 
This will also calculateyour pattern (red white blue or blue white red). 
This will also calculate factos such as: batting avg, gain/loss ratio, avg gain, avg loss, max return, max loss, and total return. 

# stock_news_sentiment: 

This program will return the sentiment analysis score of a paticular ticker for the given timeframe. It is important to read financial
news when trying to keep up with investments or researching potential invesments. Thus, a quick way of knowing if the news for a company
for any give day is good or bad is this sentiment analysis program. All values will be between -1 and +1. Positive numbers means good news
overall and negative numbers means bad news overall. Sentiment analysis is done using Vader Polarity Scores and articles are scraped using 
Beautiful Soup 4 and the website finviz.com. 

# Risk Management Calculator:

This program takes in stock information using the yfinance API. Then, it calculates the Simple movinig averages for 50 days, and 200 days. It also calculates the Exponential moving average for 21 days. 

Next, it calculates the price targets for which a person should sell their stock. Target1R, Target2R, and Target3R are the calculations of these price targets. 

Then, it will calculate the percentages from each sma/ema. If the change in percentage is greaater than the max stop loss, the display will show True, else it will show False. 
