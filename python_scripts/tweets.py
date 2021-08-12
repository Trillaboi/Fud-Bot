import tweepy
import sys

# DeItaone(bloomberg) - 2704294333
# Binance - 877807935493033984 [For tracking when new coins are listed.]
# Whale trades - 968796006576947200
# ["2343911084", "2704294333", "968796006576947200"]

class Profile:
    binance="877807935493033984"
    deItaone="2704294333"
    whaletrades="968796006576947200"
    gorillatrilla="797868177082515456"

    value_list = [binance, deItaone, whaletrades, gorillatrilla]

consumer_key = "sbszez9LQyLT1esfLf0CWBFqk"
consumer_secret = "JZfSyNwjMTLhZ0gpPe81Vn8dqapbdqymkCjvyDG8vjrLBznQhj"

access_token = "797868177082515456-TB4yAjCfJVVWuvgthDU5BaaZANp8CwF"
access_token_secret ="yrsIDmB70FsvHx9NTA6IuSRdi8yB07Yq1EOVY8ixktusl"

# An value of index 7 is used so oly append and if you delete make sure to adjust.
tracking_list = ["btc", "xbt", "ETH", "crypto", "cryptocurrency", "ETHER", "ETHEREUM", "Will List", "bitcoin"]

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

class MyStreamListener(tweepy.StreamListener):
    #status.user.screen_name
    def on_status(self, status):
        parse_tweet(status)
        # sys.stdout.flush()

    def on_error(self, status):
        print("Error")
        print(status)
       # sys.out.flush()
        
#The v2 rules would omit having to parse the data yourself but its not available with tweepy yet.
def parse_tweet(status):
    if status.user.id_str in Profile.value_list: 
        res = any(ele.upper() in status.text.upper() for ele in tracking_list)  # check if keyword is contained in the list of text
        if res:
            if "retweeted_status" not in status._json and status.in_reply_to_status_id == None:
                if status.user.id_str == Profile.binance:
                    binance_listing(status)
                else:
                    try:

                        sys.stdout.write(status.text+"\n")
                    except:
                        print("failed!!")
                        print(status)
        

def binance_listing(status):
    pass

myStreamListener = MyStreamListener()
myStream = tweepy.Stream(auth = api.auth, listener=myStreamListener)

# for tweet in tweepy.Cursor(api.search, q='tweepy').items(10):
#     print("-------\n"+tweet.text+"-------\n\n")

# default access level allows up to 400 track keywords, 5,000 follow userids and 25 0.1-360 degree location boxes


myStream.filter(follow=[Profile.binance, Profile.deItaone, Profile.whaletrades, Profile.gorillatrilla])