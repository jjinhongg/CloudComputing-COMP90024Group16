from cloudant.client import CouchDB
from cloudant.view import View
import json
import time
from collections import Counter

def update_hashtags():
    client = CouchDB('admin', 'data-miner!', url='http://172.26.133.205:5984', connect=True)
    cities = ["melbourne", "sydney", "adelaide", "canberra", "brisbane"]
    db = client['hashtags']

    hashtags = '''
    {
      "_id" : "_design/hashtags",
      "views" : {
        "all_hashtags" : {
          "map" : "function(doc){if ((!(doc.hashtags.length === 0)) && (doc.date.substr(0,4)==='2021')) {emit(doc.hashtags)}}"
        }
      }
    }
    '''
    for city in cities:
        citydb = client[city]
        djson = json.loads(hashtags)
        if djson['_id'] in citydb:
            citydb[djson['_id']].delete()
        citydb.create_document(djson)
        all_hashtags = []
        view = View(citydb['_design/hashtags'], 'all_hashtags')
        for result in view.result:
            hts = result['key']
            if type(hts[0])==dict:
                for ht in hts:
                    all_hashtags = all_hashtags + [ht['text']]
            else:
                all_hashtags = all_hashtags + hts
        top_hashtags = Counter(all_hashtags).most_common(30)
        doc = db[city]
        doc['2021'] = top_hashtags
        doc.save()