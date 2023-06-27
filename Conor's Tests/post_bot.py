import tweepy
import json, os

#Getting the API keys from external file (not on Git)
this_file = os.path.dirname(__file__)
f = open(this_file + "/api_keys.json")
data = json.load(f)

#Literally all the keys one could possibly need
api_key = data['api_key']
api_secret = data['api_secret']
access_token = data['access_token']
access_secret = data['access_secret']

bearer_token = data['bearer_token']

client_ID = data['client_ID']
client_secret = data['client_secret']

#Creating API client
client = tweepy.Client(
    consumer_key=api_key,
    consumer_secret=api_secret,
    access_token=access_token,
    access_token_secret=access_secret
)

#Posting tweet
tweet = "This is my first tweet using Tweepy"
client.create_tweet(text=tweet)