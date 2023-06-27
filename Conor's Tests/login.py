import tweepy

#My keys for API access
access_token = ""
access_secret = ""

def getUser():
    #Get user login credentials
    user_handler = tweepy.OAuth1UserHandler(
        access_token, access_secret,
        callback="oob" #For pin callback
    )

    print(user_handler.get_authorization_url(signin_with_twitter=True)) #URL needed to log in with

    code = input("Input PIN: ")

    api_key, api_secret = user_handler.get_access_token(
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