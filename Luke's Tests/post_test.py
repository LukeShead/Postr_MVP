import tweepy
import config

client = tweepy.Client(consumer_key = config.API_KEY,
                       consumer_secret = config.API_KEY_SECRET,
                       access_token = config.ACCESS_TOKEN,
                       access_token_secret = config.ACCESS_TOKEN_SECRET)

test = client.create_tweet(text="Hello World!")

print(test)