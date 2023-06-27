import tweepy

# Twitter API credentials as object
api = tweepy.Client(consumer_key = "", 
consumer_secret = "", 
access_token = "",
access_token_secret = "")

# Tweet posting function with error handling
def tweet_string(tweet):
    try:
        # Post the tweet
        api.create_tweet(text=tweet)
        print("Tweet posted successfully!")
    except tweepy.errors.TweepyException as e:
        print(f"Error: {e}")

# Prompt the user for the string to tweet
tweet_content = input("Enter the string to tweet: ")


# Tweet the string
tweet_string(tweet_content)