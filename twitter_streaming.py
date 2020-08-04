#Import the necessary methods from tweepy library
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream

#Variables that contains the user credentials to access Twitter API
access_token = ""
access_token_secret = ""
consumer_key = ""
consumer_secret = ""


keyword1 = input("Enter Keyword#1 : ")
keyword2 = input("Enter Keyword#2 : ")
keyword3 = input("Enter Keyword#3 : ")

#keyword1 = 'biden'
#keyword2 = 'trump'
#keyword3 = 'covid-19'

#This is a basic listener that just prints received tweets to stdout.
class StdOutListener(StreamListener):

    def on_data(self, data):
        if '"limit":{"track"' not in data:
            # print (data, end = '')
                with open('C:/Akash/Python/Projects/whostrending.txt','a') as tf:
                    tf.write(data)
        return True

    def on_error(self, status):
        print (status)


if __name__ == '__main__':

    #This handles Twitter authetification and the connection to Twitter Streaming API
    l = StdOutListener()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    stream = Stream(auth, l)


    print("Spooling to file in progress....Press Ctrl+C to terminate")
    #This line filter Twitter Streams to capture data by the keywords entered
    stream.filter(track=[keyword1, keyword2, keyword3])
    tf.close()
