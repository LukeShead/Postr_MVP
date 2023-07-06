import tweepy
import config


def post_tweet(message):
    try:
        client = tweepy.Client(consumer_key = config.API_KEY,
                       consumer_secret = config.API_KEY_SECRET,
                       access_token = config.ACCESS_TOKEN,
                       access_token_secret = config.ACCESS_TOKEN_SECRET)
        test = client.create_tweet(text = message)
    except tweepy.errors.TweepyException as mess:
        print(f"Error: {mess}")
