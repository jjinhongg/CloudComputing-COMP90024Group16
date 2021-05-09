from cloudant.client import CouchDB
import json

client = CouchDB('admin', 'data-miner!', url='http://172.26.133.205:5984', connect=True)

# # create a database for each city
# cities = ["melbourne", "sydney", "adelaide", "canberra", "brisbane"]
# for city in cities:
#     db = client.create_database(city)

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
            rowjson = json.loads(row)
            docid = str(rowjson["id"])
            exists = docid in citydb
            if not exists:
                newjson = {"_id": docid, "date": rowjson["date"], "time": rowjson["time"], 
                           "timezone": rowjson["timezone"], "user_id": rowjson["user_id"], "place": rowjson["place"], 
                           "tweet": rowjson["tweet"], "language": rowjson["language"], "hashtags": rowjson["hashtags"]
                          }
                doc = citydb.create_document(newjson)
            row = f.readline() 