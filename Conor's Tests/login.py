import tweepy

#My keys for API access
api_key = ""
api_secret = ""

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

    client = tweepy.Client(
        consumer_key=api_key,
        consumer_secret=api_secret,
        access_token=access_token,
        access_token_secret=access_secret
    )

    tweet = input("Type a tweet: \n")
    client.create_tweet(text=tweet)

getUser()