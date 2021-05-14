import time

from cloudant.client import CouchDB
from textblob import TextBlob
import nltk
import json
import os
from datetime import datetime
USERNAME = 'admin'
PASSWORD = 'data-miner!'
client = CouchDB(USERNAME, PASSWORD, url='http://172.26.133.205:5984', connect=True)


def couchdb_init():
    USERNAME = 'admin'
    PASSWORD = 'data-miner!'
    client = CouchDB(USERNAME, PASSWORD, url='http://172.26.133.205:5984', connect=True)
    return client

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
        # nltk.download('punkt')
        self.sentences = TextBlob(twitter).sentences
        sentence_score = 0
        for i in range(len(self.sentences)):
            sentence_score += (self.sentences[i].sentiment)[0]

        return sentence_score*100



def process_and_save(client):
    # client = couchdb_init()
    data = {'melbourne.json': 'melbourne',
            'sydney.json': 'sydney',
            'adelaide.json': 'adelaide',
            'canberra.json':'canberra',
            'brisbane.json': 'brisbane'}

    # save the preprocessed data into corresponding database
    for datafile, dbname in data.items():
        citydb = client[dbname]
        if os.path.exists(datafile):
            with open(datafile,'r',encoding='utf-8') as f:
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
                            date = rowjson["created_at"]
                            newdate = datetime.strptime(date, '%a %b %d %H:%M:%S %z %Y').strftime('%Y-%m-%d %H:%M:%S')
                            newdate = newdate.split()
                            user_id = rowjson["user"]['id']
                            newjson = {"_id": docid, "date": newdate[0], "time": newdate[1],
                                    "timezone": "+0000", "user_id": user_id,
                                    "place": rowjson["place"]['name'], "tweet": rowjson["text"],
                                    "language": rowjson["lang"], "hashtags": rowjson["entities"]['hashtags'],
                                    "sentiment": t.socre(rowjson["text"])
                                    }
                            doc = citydb.create_document(newjson)
                    except:
                        pass
                    row = f.readline()

    remove_per_hours()

def remove_per_hours():
    # time.sleep(3600)
    data = {'melbourne.json': 'melbourne',
            'sydney.json': 'sydney',
            'adelaide.json': 'adelaide',
            'canberra.json': 'canberra',
            'brisbane.json': 'brisbane'}

    # remove the json
    for datafile,_ in data.items():
        if os.path.exists(datafile):
            os.remove(datafile)


