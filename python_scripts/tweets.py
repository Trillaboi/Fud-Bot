import tweepy
import sys
import json

# DeItaone(bloomberg) - 2704294333
# Binance - 877807935493033984 [For tracking when new coins are listed.]
# Whale trades - 968796006576947200
# ["2343911084", "2704294333", "968796006576947200"]

class Profile:
    binance="877807935493033984"
    deItaone="2704294333"
    whaletrades="968796006576947200"
    gorillatrilla="797868177082515456"
    ftx="1101264495337365504"
    tier10k="2361601055"

    follow_list = [binance, deItaone, whaletrades, gorillatrilla, tier10k]

    news_list = [deItaone, tier10k]
    exchange_list = [binance, ftx]
    whale_list= [whaletrades]

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
    # The if statement below removes mentions and replies from data
    if status.user.id_str in Profile.follow_list: 
        res = any(ele.upper() in status.text.upper() for ele in tracking_list)  # check if keyword is contained in the list of text
        if res:
            if "retweeted_status" not in status._json and status.in_reply_to_status_id == None:
                tweet_dict = {"user":status.user.screen_name, "text":status.text, "userId":status.user.id_str}
                if status.user.id_str in Profile.exchange_list:
                    exchange_listing(tweet_dict)
                elif status.user.id_str in Profile.news_list:
                    crypto_news(tweet_dict)
                elif status.user.id_str in Profile.whale_list:
                    whale_trades(tweet_dict)
                else:
                    try:
                        tweet_dict['type'] = None
                        send_command(tweet_dict)
                    except:
                        print("failed!!")
                        print(status)
        

def exchange_listing(tweet_dict):
    tweet_dict['type'] = 'exchange'
    if tweet_dict["userId"] == Profile.binance:
        tweet_dict['exchange'] = 'binance'
    elif tweet_dict["userId"] == Profile.ftx:
        tweet_dict['exchange'] = 'ftx'
    else:
        tweet_dict['exchange'] = 'other'

    send_command(tweet_dict)

def crypto_news(tweet_dict):
    tweet_dict['type'] = 'news'
    send_command(tweet_dict)

def whale_trades(tweet_dict):
    tweet_dict['type'] = 'whales'
    send_command(tweet_dict)

def send_command(tweet_dict):
    sys.stdout.write(json.dumps(tweet_dict))

myStreamListener = MyStreamListener()
myStream = tweepy.Stream(auth = api.auth, listener=myStreamListener)

# for tweet in tweepy.Cursor(api.search, q='tweepy').items(10):
#     print("-------\n"+tweet.text+"-------\n\n")

# default access level allows up to 400 track keywords, 5,000 follow userids and 25 0.1-360 degree location boxes


myStream.filter(follow=Profile.follow_list)