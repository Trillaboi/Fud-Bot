import tweepy


consumer_key = "sbszez9LQyLT1esfLf0CWBFqk"
consumer_secret = "JZfSyNwjMTLhZ0gpPe81Vn8dqapbdqymkCjvyDG8vjrLBznQhj"

access_token = "797868177082515456-TB4yAjCfJVVWuvgthDU5BaaZANp8CwF"
access_token_secret ="yrsIDmB70FsvHx9NTA6IuSRdi8yB07Yq1EOVY8ixktusl"

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

class MyStreamListener(tweepy.StreamListener):
    
    def on_status(self, obj):
        print(obj.user.screen_name)
    
    def on_error(self, obj):
        print(obj)
        

def parse_tweet(tweet):
    pass


myStreamListener = MyStreamListener()
myStream = tweepy.Stream(auth = api.auth, listener= myStreamListener)

# for tweet in tweepy.Cursor(api.search, q='tweepy').items(10):
#     print("-------\n"+tweet.text+"-------\n\n")

# DeItaone - 2704294333
# ["2343911084", "2704294333", "968796006576947200"]
myStream.filter(follow=["2343911084"])