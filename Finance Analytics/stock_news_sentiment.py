from urllib.request import urlopen, Request
from bs4 import BeautifulSoup
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import pandas as pd
import matplotlib.pyplot as plt

finwiz_url = 'https://finviz.com/quote.ashx?t='

tickers = ['AMZN','GOOG', 'FB']

news_tables ={} # dictonary that is holding the tables values
for ticker in tickers:
    url = finwiz_url + ticker

    req = Request(url=url, headers={'user-agent':'my-app'})
    response = urlopen(req)

    html = BeautifulSoup(response, 'html')
    news_table = html.find(id='news-table') # using bs4 to find the ID for the tables in the code to parse through the articles
    news_tables[ticker]= news_table   # storing the table object inside our dictonary


parsed_data = []

for ticker, news_table in news_tables.items():
    for row in news_table.findAll('tr'):
        title = row.a.get_text()
        date_data = row.td.text.split(' ')

        if len(date_data)==1:
            time = date_data[0]
        else:
            date = date_data[0]
            time = date_data[1]

        parsed_data.append([ticker, date, time, title])

# Apply sentiment analysis

df = pd.DataFrame(parsed_data, columns=['ticker', 'date', 'time', 'title'])

vader = SentimentIntensityAnalyzer()

f = lambda title: vader.polarity_scores(title)['compound']  # Appy Sentiment to titles and create a new df called compound to hold scores
df['compound'] = df['title'].apply(f)

# Visualize the sentiment

df['date'] = pd.to_datetime(df.date).dt.date   # Take date and convert from string to datetime data

plt.figure(figsize=(10,8))
mean_df = df.groupby(['ticker','date']).mean()  # return df of ticker and date and avg value of compounjd values for that day
# Unstack data
mean_df = mean_df.unstack()
mean_df = mean_df.xs('compound', axis="columns").transpose()
mean_df.plot(kind='bar')
plt.show()
