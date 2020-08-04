import json
import pandas as pd
import matplotlib.pyplot as plt
import re

tweets_data_path = 'C:/Akash/Python/Projects/whostrending.txt'

keyword1 = input("Enter Keyword#1 : ")
keyword2 = input("Enter Keyword#2 : ")
keyword3 = input("Enter Keyword#3 : ")

#keyword1 = 'biden'
#keyword2 = 'trump'
#keyword3 = 'covid-19'

tweets_data = []
tweets_file = open(tweets_data_path, "r")
for line in tweets_file:
    try:
        tweet = json.loads(line)
        tweets_data.append(tweet)
    except:
        continue





print ('There are ' + str(len(tweets_data)) + ' tweets in the file ' + tweets_data_path)

if len(tweets_data) < 100:
	pd.set_option('display.max_rows', None)

tweets = pd.DataFrame()

tweets['text'] = list(map(lambda tweet: tweet['text'], tweets_data))
tweets['lang'] = list(map(lambda tweet: tweet['lang'], tweets_data))
tweets['country'] = list(map(lambda tweet: tweet['place']['country'] if tweet['place'] != None else 'Not Available', tweets_data))


tweets_by_lang = tweets['lang'].value_counts()

print ('There are ' + str(len(tweets_by_lang)) + ' distinct languages in the file ' + tweets_data_path)

print (tweets_by_lang)

fig, ax = plt.subplots()
ax.tick_params(axis='x', labelsize=15)
ax.tick_params(axis='y', labelsize=10)
ax.set_xlabel('Languages', fontsize=15)
ax.set_ylabel('Number of tweets' , fontsize=15)
ax.set_title('Top 5 languages', fontsize=15, fontweight='bold')
tweets_by_lang[:5].plot(ax=ax, kind='bar', color='red')

plt.show()


tweets_by_country = tweets['country'].value_counts()

print ('There are ' + str(len(tweets_by_country)) + ' distinct countries in the file ' + tweets_data_path)
print (tweets_by_country)

fig, ax = plt.subplots()
ax.tick_params(axis='x', labelsize=15)
ax.tick_params(axis='y', labelsize=10)
ax.set_xlabel('Countries', fontsize=15)
ax.set_ylabel('Number of tweets' , fontsize=15)
ax.set_title('Top 5 countries', fontsize=15, fontweight='bold')
tweets_by_country[:5].plot(ax=ax, kind='bar', color='blue')

plt.show()

print(tweets)


def word_in_text(word, text):
    word = word.lower()
    text = text.lower()
    match = re.search(word, text)
    if match:
        return True
    return False

tweets[keyword1] = tweets['text'].apply(lambda tweet: word_in_text(keyword1, tweet))
tweets[keyword2] = tweets['text'].apply(lambda tweet: word_in_text(keyword2, tweet))
tweets[keyword3] = tweets['text'].apply(lambda tweet: word_in_text(keyword3, tweet))

print ('Keyword1 (' + keyword1 + ')' + str(tweets[keyword1].value_counts()[True]))
print ('Keyword2 (' + keyword2 + ')' + str(tweets[keyword2].value_counts()[True]))
print ('Keyword3 (' + keyword3 + ')' + str(tweets[keyword3].value_counts()[True]))


list_keywords = [keyword1,keyword2,keyword3]


tweets_by_keywords = [tweets[keyword1].value_counts()[True], tweets[keyword2].value_counts()[True], tweets[keyword3].value_counts()[True]]

x_pos = list(range(len(list_keywords)))
width = 0.8
fig, ax = plt.subplots()
plt.bar(x_pos, tweets_by_keywords, width, alpha=1, color='g')

# Setting axis labels and ticks
ax.set_ylabel('Number of tweets', fontsize=15)
ax.set_title('Ranking: ' + keyword1 + ' vs. ' + keyword2 + ' vs. ' + keyword3, fontsize=10, fontweight='bold')
ax.set_xticks([p + 0.4 * width for p in x_pos])
ax.set_xticklabels(list_keywords)
plt.grid()

plt.show()

print ('Done')
