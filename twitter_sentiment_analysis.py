import tweepy # used to gain access to Twitter's APIs
from textblob import TextBlob # used for sentiment analysis

# keys used as part of Twitter's API
CONSUMER_KEY = 'your_consumer_key' # created as part of registration of client applicaiton
CONSUMER_SECRET = "your_consumer_secret" # created as part of registration of client application
ACCESS_TOKEN = 'your_access_token'
ACCESS_TOKEN_SECRET = 'your_access_token_secret'

# create tweepy API instance via OAuth authentication
auth = tweepy.OAuthHandler(consumer_key, consumer_key_secret) # create OAuthHandler instance
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth) # create api instance

subject_tweets = api.search('Cars') # returns tweets related to the subject matter 'Cars'

# iterate over subject_tweets array and check sentiment of each tweet
for tweet in subject_tweets:
	print(tweet.text)
	analysis = TextBlob(tweet.text) # returns polarity and subjectivity floats
	print(analysis.sentiment)
	if analysis.sentiment[0]>0: # sentiment analysis based only on polarity
		print 'Positive'
	else:
		print 'Negative'
	print("")