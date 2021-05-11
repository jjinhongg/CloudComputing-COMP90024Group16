from cloudant.client import CouchDB
from cloudant.view import View
import json
import time
from collections import Counter

date = '''
{
  "_id" : "_design/date",
  "views" : {
    "year_count" : {
      "map" : "function(doc){emit(doc.date.substr(0,4))}",
      "reduce" : "_count"
    },
    "month_count" : {
      "map" : "function(doc){emit(doc.date.substr(0,7))}",
      "reduce" : "_count"
    }
  }
}
'''

language = '''
{
  "_id" : "_design/language",
  "views" : {
    "lang_count" : {
      "map" : "function(doc){emit(doc.language)}",
      "reduce" : "_count"
    }
  }
}
'''

sentiment = '''
{
  "_id" : "_design/sentiment",
  "views" : {
    "senti_sum" : {
      "map" : "function(doc){emit(doc.date.substr(0,4),doc.sentiment)}",
      "reduce" : "_sum"
    }
  }
}
'''

hour = '''
{
  "_id" : "_design/hour",
  "views" : {
    "hour_count" : {
      "map" : "function(doc){emit(doc.time.substr(0,2))}",
      "reduce" : "_count"
    }
  }
}
'''

hashtags = '''
{
  "_id" : "_design/hashtags",
  "views" : {
    "all_hashtags" : {
      "map" : "function(doc){emit(doc.hashtags)}"
    }
  }
}
'''

client = CouchDB('admin', 'data-miner!', url='http://172.26.133.205:5984', connect=True)

cities = ["melbourne", "sydney", "adelaide", "canberra", "brisbane"]

for city in cities:
    citydb = client[city]
    for dstr in [date, language, sentiment, hour, hashtags]:
        djson = json.loads(dstr)
        if not djson['_id'] in citydb:
            citydb.create_document(djson)

# current tweet number for this month
current_twts = {}
number = 0
for city in cities:
    citydb = client[city]
    view = View(citydb['_design/date'], 'month_count')
    with view.custom_result(group=True) as results:
        for result in results:
            if result['key'] == time.strftime("%Y-%m", time.localtime()):
                number = number + result['value']
current_twts['number'] = number
with open('current_twts.json','w') as f:
    f.write(json.dumps(current_twts))

# total tweet number each year each city 
total_twts = {}
for city in cities:
    citydb = client[city]
    year_count = {}
    view = View(citydb['_design/date'], 'year_count')
    with view.custom_result(group=True) as results:
        for result in results:
            year_count[result['key']] = result['value']
    total_twts[city] = year_count
with open('total_twts.json','w') as f:
    f.write(json.dumps(total_twts))
    
# language distribution each city
lang_dis = {}
for city in cities:
    citydb = client[city]
    lang_count = {}
    view = View(citydb['_design/language'], 'lang_count')
    with view.custom_result(group=True) as results:
        for result in results:
            if result['key'] != 'und':
                lang_count[result['key']] = result['value']
    lang_dis[city] = lang_count
with open('lang_dis.json','w') as f:
    f.write(json.dumps(lang_dis))
    
# average sentiment score each year each city
senti_score = {}
for city in cities:
    citydb = client[city]
    senti_avg = {}
    view = View(citydb['_design/sentiment'], 'senti_sum')
    with view.custom_result(group=True) as results:
        for result in results:
            senti_avg[result['key']] = result['value']/total_twts[city][result['key']]
    senti_score[city] = senti_avg
with open('senti_score.json','w') as f:
    f.write(json.dumps(senti_score))
    
# time(hour) distribution each city (UTC+10)
time_dis = {}
for city in cities:
    citydb = client[city]
    hour_prop = {}
    view = View(citydb['_design/hour'], 'hour_count')
    with view.custom_result(group=True) as results:
        for result in results:
            hour_prop[(int(result['key'])+2)%24] = result['value']/sum(total_twts[city].values())
    time_dis[city] = hour_prop
with open('time_dis.json','w') as f:
    f.write(json.dumps(time_dis))
    
# top 30 used hashtags each city
top_hashtags = {}
for city in cities:
    citydb = client[city]
    all_hashtags = []
    view = View(citydb['_design/hashtags'], 'all_hashtags')
    for result in view.result:
        all_hashtags = all_hashtags + result['key']
    hashtags_count = dict(Counter(all_hashtags))
    hashtags_sorted = sorted(hashtags_count.items(),key = lambda x:x[1],reverse = True)[0:30]
    top_hashtags[city] = dict(hashtags_sorted)
with open('top_hashtags.json','w') as f:
    f.write(json.dumps(top_hashtags))