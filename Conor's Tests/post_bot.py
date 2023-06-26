import tweepy

api_key = ""
api_secrets = ""
access_token = ""
access_secret = ""

bearer_token = ""

# Authenticate to Twitter
#auth = tweepy.OAuth1UserHandler(
auth = tweepy.OAuth2AppHandler(
   consumer_key=api_key,
   consumer_secret=api_secrets
   #bearer_token
   )

client = tweepy.Client(
    api_key,
    api_secrets,
    access_token,
    access_secret
)
 
api = tweepy.API(client)

tweet = "This is my first tweet using Tweepy"
#client.create_tweet(tweet)
api.update_status(status=tweet)