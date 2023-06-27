import tweepy
import json, os

#Getting the API keys from external file (not on Git)
this_file = os.path.dirname(__file__)
f = open(this_file + "/api_keys.json")
data = json.load(f)

#My keys for API access
api_key = data['api_key']
api_secret = data['api_secret']

def getUser():
    #Get user login credentials
    user_handler = tweepy.OAuth1UserHandler(
        api_key, api_secret,
        callback="oob" #For pin callback
    )

    print(user_handler.get_authorization_url()) #URL needed to log in with

    code = input("Input PIN: ")

    access_token, access_secret = user_handler.get_access_token(
        code
    ) # get keys with pin
    return access_token, access_secret

def post_tweet():
    access_token, access_secret = getUser()
    client = tweepy.Client(
        consumer_key=api_key,
        consumer_secret=api_secret,
        access_token=access_token,
        access_token_secret=access_secret
    )

    tweet = input("Type a tweet: \n")
    client.create_tweet(text=tweet)
