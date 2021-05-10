from cloudant.client import CouchDB
from textblob import TextBlob
import nltk
import json
import twint
import time
USERNAME = 'admin'
PASSWORD = 'data-miner!'
client = CouchDB(USERNAME, PASSWORD, url='http://172.26.133.205:5984', connect=True)

def create_db():
    # create a database for each city   
    cities = ["melbourne", "sydney", "adelaide", "canberra", "brisbane"]
    for city in cities:
        db = client.create_database(city)


class SentimentScore():
    '''
    input： whole twitter text
    output: this text sentiment score
    '''
    def __init__(self):
        self.sentences = []

    def socre(self,twitter):
        nltk.download('punkt')
        self.sentences = TextBlob(twitter).sentences
        sentence_score = 0
        for i in range(len(self.sentences)):
            sentence_score += (self.sentences[i].sentiment)[0]

        return sentence_score*100


def tweetCrawling(location, coordinate, range,date):
    outputf = '.'.join([location, "json"])
    # print(outputf)
    c = twintCongig(coordinate, range, outputf,date)
    twint.run.Search(c)

def twintCongig(coordinate, range, outputf,date):
    geo = ",".join([str(coordinate[0]), str(coordinate[1]), range])
    c = twint.Config()
    c.Geo = geo
    # c.Since = "2019-01-01"
    c.Until = date
    # c.Limit = 5000000
    c.Output = outputf
    c.Store_json = True
    return c

def run_spider():
    time_record = "2019-05-09"
    while True:
        cities = ["Melbourne", "Sydney",
                  "Adelaide", "Canberra",
                  "Brisbane"]
        cities_geo = {"Melbourne": (-37.8136, 144.9631), "Sydney": (-33.8688, 151.2093),
                  "Adelaide": (-34.9285, 138.6007), "Canberra": (-35.2809, 149.1300),
                  "Brisbane": (-27.4705, 153.0260)}
        if time_record != time.strftime("%Y-%m-%d", time.localtime()):
            for city in cities:
                tweetCrawling(city, cities_geo[city], "20km",time_record)

            time_record = time.strftime("%Y-%m-%d", time.localtime())

def process_and_save():
    while True:
        data = {'Melbourne.json': 'melbourne',
                'Melbourne2.json': 'melbourne',
                'Sydney.json': 'sydney',
                'Sydney2.json': 'sydney',
                'Adelaide.json': 'adelaide',
                'Adelaide2.json': 'adelaide',
                'Canberra.json':'canberra',
                'Brisbane.json': 'brisbane',
                'Brisbane2.json': 'brisbane'}

        # save the preprocessed data into corresponding database
        for datafile, dbname in data.items():
            citydb = client[dbname]
            with open(datafile,'r') as f:
                row = f.readline()
                while(row):
                    try:
                        rowjson = json.loads(row)
                        docid = str(rowjson["id"])
                        exists = docid in citydb
                        if exists:
                            print("Tweet {} already stored in {} db!".format(docid, dbname))
                        if not exists:
                            t = SentimentScore()
                            newjson = {"_id": docid, "date": rowjson["date"], "time": rowjson["time"],
                                    "timezone": rowjson["timezone"], "user_id": rowjson["user_id"],
                                    "place": rowjson["place"], "tweet": rowjson["tweet"],
                                    "language": rowjson["language"], "hashtags": rowjson["hashtags"],
                                    "sentiment": t.socre(rowjson["tweet"])
                                    }
                            doc = citydb.create_document(newjson)
                    except:
                        pass
                    row = f.readline()