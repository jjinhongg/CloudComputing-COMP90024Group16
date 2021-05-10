from cloudant.client import CouchDB
import cloudant
USERNAME = 'admin'
PASSWORD = 'data-miner!'
client = CouchDB(USERNAME, PASSWORD, url='http://172.26.133.205:5984', connect=True)

session = client.session()
print('Username: {}'.format(session['userCtx']['name']))
print('Databases: {}'.format(client.all_dbs()))

mydesign = '''
{
  "_id" : "_design/mydesign",
  "views" : {
    "lang_count" : {
      "map" : "function(doc){emit(doc.language)}",
      "reduce" : "_count"
    },
    "all_hashtags" : {
      "map" : "function(doc){if(!(doc.hashtags.length === 0)) {emit(doc.hashtags)}}"
    },
    "time_count" : {
      "map" : "function(doc){emit(doc.time.substr(0,2))}",
      "reduce" : "_count"
    },
    "get_text" : {
      "map" : "function(doc){emit(doc.tweet)}"
    }
  }
}
'''

cities = ["melbourne", "sydney", "adelaide", "canberra", "brisbane"]
for city in cities:
    citydb = client[city]
    citydb.create_document(json.loads(mydesign))

# db = client['melbourne']
# ddoc = cloudant.design_document.DesignDocument(db, document_id='design')
# ddoc.add_view('lang', 'function(doc){emit(doc.language, 1);}', '_count')
# ddoc.save()

# view = cloudant.view.View(ddoc, 'lang')
# result = db.get_view_result('_design/design', 'lang', group = True, reduce = True, raw_result=True)


# http://172.26.133.205:5984/melbourne/_design/design/_view/lang?group=true&reduce=true

# output = result['rows']
# for item in output:
#     print(item)
