#Twitter Sentiment Analyzer
import tweepy
from textblob import TextBlob
import csv

consumer_key = 'TOKEN_HERE'
consumer_secret = 'TOKEN_HERE'

access_token = 'TOKEN_HERE'
access_token_secret = 'TOKEN_HERE'

auth = tweepy.OAuthHandler(consumer_key,consumer_secret)
auth.set_access_token(access_token,access_token_secret)

api = tweepy.API(auth)

search_string = input()

#Searches for the tweets containing the input string
public_tweets = api.search(search_string)

#Creating a list of tweets and their polarity
public_data = []
for tweet in public_tweets:
	#print(tweet.text)
	data = TextBlob(tweet.text)
	#print(data.sentiment.polarity)
	public_data.append([tweet.text,data.sentiment.polarity])
print(public_data)

#Writes the data as [tweet,sentiment] to a CSV File
myFile = open('twitterdata1.csv', 'w')  
with myFile:  
   writer = csv.writer(myFile)
   writer.writerows(public_data)
print('Writing Success')
    
