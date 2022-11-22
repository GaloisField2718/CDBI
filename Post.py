from urllib import response
import config
import tweepy

client = tweepy.Client(consumer_key=config.API_KEY, consumer_secret=config.API_KEY_SECRET, access_token=config.ACCESS_TOKEN, access_token_secret=config.ACCESS_TOKEN_SECRET)



response = client.create_tweet(text="Hello everyone, this post was made through an automation and voted on AstroDAO : https://testnet.app.astrodao.com/dao/nearcontest.sputnikv2.testnet")

print(f"https://twitter.com/user/status/{response.data['id']}")


""" We can use only the Bearer Token to make a tweet query """

# bearer_token = config.BEARER_TOKEN
# query = 'Blockchain NearProtocol'

# response = client.search_recent_tweets(query = query, max_results = 10)

# print(response)


"""Maybe the Token which provides access to DM """

#client.get_dm_events

#print(client.get_dm_events)

