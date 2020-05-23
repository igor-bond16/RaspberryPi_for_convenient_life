import tweepy
import webbrowser
import schedule
import time

#tweets_data = []
tweet_id = [1263998127721246721,
 1263620617124720640,
 1263398638157352960,
 1263375130467504128,
 1262887245473697792,
 1262294134095622145,
 1261896484355584000,
 1261786338426097665,
 1261621703563608064,
 1260851820231942144,
 1260328318114512896,
 1259830049663942657,
 1259703236946092032,
 1259689115970232322,
 1258379611156516864,
 1257976346254307330,
 1257851343655407618,
 1257800516395921408,
 1257510220730781698,
 1257488982226558976]


api_key = 'frE4CnToQxPd4tohEHrXNq9FE'
secret_key = 'xstamsCZvVFmCMLyT4gNnF2zt9n5WxFmJVnokLayiGEvY2RsQ8'
callback_uri = 'oob'
awth = tweepy.OAuthHandler(api_key,secret_key,callback_uri)
redirect_url = awth.get_authorization_url()
webbrowser.open(redirect_url)
user_pint_input = input("What's the pin value? ")
awth.get_access_token(user_pint_input)
api = tweepy.API(awth,wait_on_rate_limit=True)
my_timeline = api.home_timeline()



def get_tweets_id():
    columns = set()
    allowed_types = [str,int]
    tweets_data = []
    for status in my_timeline:
        status_dict = dict(vars(status))
        keys = status_dict.keys()
        single_tweet_data = {'User':status.user.screen_name,'author':status.author.screen_name}
        for k in keys:
            try:
                v_type = type(status_dict[k])
            except:
                v_type = None
            if v_type != None:
                if v_type in allowed_types:
                    single_tweet_data[k] = status_dict[k]
                    columns.add(k)
        tweets_data.append(single_tweet_data['id'])
    return tweets_data

def like_and_retweet(_id):
    api.retweet(_id)
    tweet_id.append(_id)
    api.create_favorite(_id)

def main():
    run = True
    while run:
        try:
            for _id in get_tweets_id():
                if not _id in tweet_id:
                    like_and_retweet(_id)
        except KeyboardInterrupt:
            run = False



schedule.every(1).minutes.do(main)

while True:
    schedule.run_pending()
    time.sleep(1)
    