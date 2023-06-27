import tweepy
import config


client = tweepy.Client(bearer_token = config.BEARER_TOKEN)

query = "ukraine russia -is:retweet"

response = client.search_recent_tweets(query=query, max_results = 100)

print(response)