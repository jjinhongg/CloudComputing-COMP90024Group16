from cloudant.client import CouchDB
from textblob import TextBlob
import nltk
import json
import os
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



def process_and_save():
    data = {'Melbourne.json': 'melbourne',
            'Sydney.json': 'sydney',
            'Adelaide.json': 'adelaide',
            'Canberra.json':'canberra',
            'Brisbane.json': 'brisbane'}

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

def remove_per_hours():
    data = {'Melbourne.json': 'melbourne',
            'Sydney.json': 'sydney',
            'Adelaide.json': 'adelaide',
            'Canberra.json': 'canberra',
            'Brisbane.json': 'brisbane'}

    # remove the json
    for datafile,_ in data.items():
        if os.path.exists(datafile):
            os.remove(datafile)