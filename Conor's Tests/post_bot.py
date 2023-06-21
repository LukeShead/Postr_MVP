import tweepy

api_key = ""
api_secrets = ""
access_token = ""
access_secret = ""

# Authenticate to Twitter
auth = tweepy.OAuth1UserHandler(
   api_key, api_secrets,
   access_token, access_secret
)
 
api = tweepy.API(auth)

tweet = "This is my first tweet using Tweepy"
api.update_status(status=tweet)