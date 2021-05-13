from cloudant.client import Cloudant
import tweepy
from tweepy.streaming import StreamListener
from tweepy import Stream
import json as js
import argparse
from datetime import datetime
import time
import json

# My keys and tokens

USERNAME = 'admin'
PASSWORD = 'data-miner!'
URL = 'http://172.26.133.205:5984'
client = Cloudant(USERNAME, PASSWORD, url=URL, connect=True, auto_renew=True)
print(client.all_dbs())
db = client.create_database('mydb', partitioned=False)

config_file = 'config.json'

def load_config():
    with open(config_file, 'rb') as f:
        config = json.loads(f.read())
        return config

config = load_config()

def get_account(key: str):
    return config.get('accounts').get(key)

def getAuth(account_key: str):
    account = get_account(account_key)

    consumer_key = account.get('consumer_key')
    consumer_secret = account.get('consumer_secret')
    access_token = account.get('access_token')
    access_token_secret = account.get('access_token_secret')

    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)

    return auth

def dealStream(tweetJson, file):

    try:
        
        dataDict = {}
        dataDict["id"] = tweetJson["id_str"]
        dataDict["user"] = tweetJson["user"]["screen_name"]
        dataDict["text"] = tweetJson["text"]

        if tweetJson["created_at"] != None:
            stringTime = tweetJson["created_at"]
            dataDict["date"] = datetime.strptime(stringTime,'%a %b %d %H:%M:%S %z %Y').strftime('%Y-%m-%d %H:%M:%S%z')
        else:
            dataDict["date"] = ""
            
        dataDict["hashtags"] = []

        if tweetJson["entities"]["hashtags"] != None:

            listHashtags = tweetJson["entities"]["hashtags"]
            for hashtag in listHashtags:        
                dataDict["hashtags"].append(hashtag["text"])

        elif tweetJson["extended_tweet"] != None and tweetJson["extended_tweet"]["entities"] != None and\
             tweetJson["extended_tweet"]["entities"]["hashtags"] != None:
            
            listHashtags = tweetJson["extended_tweet"]["entities"]["hashtags"]
            for hashtag in listHashtags:        
                dataDict["hashtags"].append(hashtag["text"])            

        if tweetJson["coordinates"]!= None and tweetJson["coordinates"]["coordinates"] != None:
            dataDict["geo"] = tweetJson["coordinates"]["coordinates"]

        elif tweetJson["geo"]!= None and tweetJson["geo"]["coordinates"] != None:
            temp = tweetJson["geo"]["coordinates"]
            if len(temp) == 2:
                dataDict["geo"] = [temp[1], temp[0]]
        else:
            dataDict["geo"] = []
        
        
        newJson = js.dumps(dataDict) 
        

    except Exception as e:

        print(e)
        print("Cannot upload a well-formatted tweet to couchDB")
        file.write(str(e) + "\n")
        file.write("Cannot upload a well-formatted tweet to couchDB\n")
        time.sleep(30)
        
    return newJson

parser = argparse.ArgumentParser(description='COMP90024 Project Twitter Streamer')
# Use like:
# python arg.py -l 1234 2345 3456 4567
parser.add_argument('-l','--list', nargs='+', default=[141, -38, 150, -34])
parser.add_argument('--filename', type=str, default="streamlog.txt")
args = parser.parse_args()

file = open(args.filename, "w")

#This is a basic listener that just prints received tweets to stdout.
class TweetListener(StreamListener):

    def on_data(self, data):

        tweetJson = js.loads(data, encoding= 'utf-8')
        
    	# need to filter out the retweet
        if not tweetJson["text"].startswith('RT') and tweetJson["retweeted"] == False:
            file.write(data)
            db.create_document(tweetJson)
            
            newJSON = dealStream(tweetJson, file)
            tweetJson = js.loads(newJSON, encoding= 'utf-8')
            # db.create_document(tweetJson)
            print(newJSON)
        return True

    def on_error(self, status):
        print (status)
        if status == 420:
            #returning False in on_data disconnects the stream
            return False

if __name__ == '__main__':

    #This handles Twitter authetification and the connection to Twitter Streaming API
    listener = TweetListener()
    auth = getAuth('wenqinl2')
    stream = Stream(auth, listener)

    #This line filter Twitter Streams to capture data around Victoria state
    stream.filter(locations=args.list) 

    file.close()


