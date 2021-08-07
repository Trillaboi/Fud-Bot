import tweepy


consumer_key = "sbszez9LQyLT1esfLf0CWBFqk"
consumer_secret = "JZfSyNwjMTLhZ0gpPe81Vn8dqapbdqymkCjvyDG8vjrLBznQhj"

access_token = "797868177082515456-TB4yAjCfJVVWuvgthDU5BaaZANp8CwF"
access_token_secret ="yrsIDmB70FsvHx9NTA6IuSRdi8yB07Yq1EOVY8ixktusl"

tracking_list = ["btc", "xbt", "ETH", "crypto", "cryptocurrency", "ETHER", "ETHEREUM"]


auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

class MyStreamListener(tweepy.StreamListener):
    #status.user.screen_name
    def on_status(self, status):
        parse_tweet(status)

    def on_error(self, status):
        print(status)

        
# The v2 rules would omit having to parse the data yourself but its not available with tweepy yet.
def parse_tweet(status):
    res = any(ele in status.text for ele in tracking_list)
    if res:
        print(status.text)
    


myStreamListener = MyStreamListener()
myStream = tweepy.Stream(auth = api.auth, listener= myStreamListener)

# for tweet in tweepy.Cursor(api.search, q='tweepy').items(10):
#     print("-------\n"+tweet.text+"-------\n\n")

# default access level allows up to 400 track keywords, 5,000 follow userids and 25 0.1-360 degree location boxes


# DeItaone - 2704294333
# ["2343911084", "2704294333", "968796006576947200"]

myStream.filter(follow=["968796006576947200", "2704294333"])