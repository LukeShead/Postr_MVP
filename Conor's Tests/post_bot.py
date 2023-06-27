import tweepy

api_key = ""
api_secret = ""
access_token = ""
access_secret = ""

bearer_token = ""

client_ID = ""
client_secret = ""

client = tweepy.Client(
    consumer_key=api_key,
    consumer_secret=api_secret,
    access_token=access_token,
    access_token_secret=access_secret
)

tweet = "This is my first tweet using Tweepy"
client.create_tweet(text=tweet)