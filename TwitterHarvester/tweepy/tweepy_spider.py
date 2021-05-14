import tweepy
import json
import time

def tweepy_init():
    '''
    init the tweepy account
    :return:  accout
    '''
    # config = None
    # with open('config.json', 'rb') as f:
    #     config = json.loads(f.read())
    # key = 'zixuanz'
    # account = config.get('accounts').get(key)

    # consumer_key = account.get('consumer_key')
    # consumer_secret = account.get('consumer_secret')
    # access_token = account.get('access_token')
    # access_token_secret = account.get('access_token_secret')
 
    consumer_key = "NlxfH8KHuVhKUPZZeSh90y12o"
    consumer_secret = "wJWb1D0qqM9b2nikhKy2ZTXus5acV6yQoHVCs6WJC1MzegsEKD"
    access_token = "1367986631983046658-mMydlFKzFPtRPrZW13TTikgyHdpIaw"
    access_token_secret = "EJR6yGb2HTgj4mkHa1joXj5tZspLhdA3hFkbCwiCzZicH"

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
    api = tweepy_init()
    # available_loc = api.trends_available()

    for datafile, dbname in data.items():
        # loc = dbname
        # g = geocoder.osm(loc)
        # closest_loc = api.geo_search(g.lat, g.lng)
        # print(closest_loc)
        all_tweets = []
        places = api.geo_search(query=dbname, granularity="city")
        place_id = places[0].id
        tweets = api.search(q="place:%s" % place_id)
        # print(tweets[0])
        for i in range(len(tweets)):
            all_tweets.append(tweets[i])

        # trends = api.trends_place(closest_loc[0]['woeid'])
        with open("{}.json".format(dbname), "w") as wp:
            for i in range(len(all_tweets)):
                wp.write(json.dumps(tweets[i]._json)+'\n')


    time.sleep(100)


