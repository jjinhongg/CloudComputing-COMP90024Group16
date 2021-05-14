import tweepy
import json
import time
import random
from datetime import datetime
def account_info():

    account = {
        "accounts": {
            "wenqinl": {
                "consumer_key": "U1lUxhPRqkgJnjcYxzR9l882D",
                "consumer_secret": "eWyY3NaI02ZmNXT3V4ITbPGGWvrGzUyb6Lr71ecfraw8VaYQ3i",
                "access_token": "1118399076653944833-cpAmEuFX694kK4i7JSQy9DnRzsfZG9",
                "access_token_secret": "Wh3MzRqIwqXcymvRcticPRkewb06s8DuuRiHvEXEQDdjm"
            },

            "wenqinl2": {
                "consumer_key": "T6naC4HnDDzbr4oSHO4X2SxPt",
                "consumer_secret": "amFPzphkau0VfdJcMpZ4ibDpqn7ILYpvwLxTNN4F8JhEgT45E1",
                "access_token": "30395342-cv5GgAO6CT5bKfjkfjNd0M5o0eemRT4eOaVZgDNUy",
                "access_token_secret": "zCYZAyPZONpBV3iYZdnakUwgMBGY4nqP0OU0EemmxjNW9"
            },

            "zixuanz": {
                "consumer_key": "NlxfH8KHuVhKUPZZeSh90y12o",
                "consumer_secret": "wJWb1D0qqM9b2nikhKy2ZTXus5acV6yQoHVCs6WJC1MzegsEKD",
                "access_token": "1367986631983046658-mMydlFKzFPtRPrZW13TTikgyHdpIaw",
                "access_token_secret": "EJR6yGb2HTgj4mkHa1joXj5tZspLhdA3hFkbCwiCzZicH"
            },

            "jinyongy": {
                "consumer_key": "MYIJ96NtNqPKL7smamIlMcuD8",
                "consumer_secret": "L868VsEU4bZnUM3AJODNqHz1fpRIIBhlXwE8M4RNf1dgO4ryrF",
                "access_token": "1366207880727203843-Kng0F2UMDtErS0g6QTGKMSTXTER3Hs",
                "access_token_secret": "hXKUGE1h1MgoFkuZ5xOayqkw0qxaRXOia7XdBRzzKIMca"
            },

            "new1": {
                "consumer_key": "9yzZucgdrZ92SH9Sy1HC0kqRR",
                "consumer_secret": "YlCvDefeX61wsUAFpG8v6yeU8EJWAhuePQWutZoMGQ6iZt5L3j",
                "access_token": "1257681698373775360-eDwFqLAycB1EWE42VMntCnMCA4djEU",
                "access_token_secret": "H4u1GKTpluZHOVj5SRy0XgURuMtl7E7WV6TtoZk2v6QvP"
            }
        },

        "target_location": {
            "melbourne": [[-38.465387, 144.566830], [-37.517320, 145.401791]],
            "australia": [[-45.134095, 109.041799], [-11.585642, 153.162890]]
        },

        "db": {
            "user": "admin",
            "password": "data-miner!",
            "url": "http://172.26.133.205:5984"
        }
    }

    return account

def tweepy_init():
    '''
    init the tweepy account
    :return:  accout
    '''
    config = account_info()

    key_list = ['wenqinl','wenqinl2','zixuanz','jinyongy','new1']
    key = random.choice(key_list)
    print('current account:',key)
    account = config.get('accounts').get(key)

    consumer_key = account.get('consumer_key')
    consumer_secret = account.get('consumer_secret')
    access_token = account.get('access_token')
    access_token_secret = account.get('access_token_secret')

    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth,wait_on_rate_limit=True)
    return api

def run_spider():
    data = {'Melbourne.json': 'melbourne',
            'Sydney.json': 'sydney',
            'Adelaide.json': 'adelaide',
            'Canberra.json': 'canberra',
            'Brisbane.json': 'brisbane'}
    cities_geo = {"melbourne": (-37.8136, 144.9631), "sydney": (-33.8688, 151.2093),
                  "adelaide": (-34.9285, 138.6007), "canberra": (-35.2809, 149.1300),
                  "brisbane": (-27.4705, 153.0260)}
    api = tweepy_init()
    # available_loc = api.trends_available()

    for datafile, dbname in data.items():
        # loc = dbname
        # g = geocoder.osm(loc)
        # closest_loc = api.geo_search(g.lat, g.lng)
        # print(closest_loc)
        coordinates = str(cities_geo[dbname][0])+','+str(cities_geo[dbname][1])+ ',20km'
        result_type = 'recent'
        until_date = '2021-5-10'
        max_tweets = 1000

        tweets = tweepy.Cursor(api.search, geocode=coordinates,result_type=result_type,
                               until=until_date, count=100).items(max_tweets)
        alltw = []
        for tweet in tweets:
            cur = tweet._json
            alltw.append(cur)

        with open("{}.json".format(dbname), "w") as wp:
            for i in range(len(alltw)):
                wp.write(json.dumps(alltw[i]) + '\n')
        # places = api.geo_search(query=dbname, granularity="city")
        # for i in range(len(places)):
        #     place_id = places[i].id
        #     # print(place_id)
        #     tweets = api.search(q="place:%s" % place_id)
            # all_tweets = []
            # print(tweets[0])
            # for k in range(len(tweets)):
            #     all_tweets.append(tweets[k])

        # with open("{}.json".format(dbname), "w") as wp:
        #     wp.write(json.dumps(newjson)+'\n')


    time.sleep(100)



