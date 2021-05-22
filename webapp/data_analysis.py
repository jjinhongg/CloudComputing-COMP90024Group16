from cloudant.client import CouchDB
from cloudant.view import View
from cloudant.result import Result
import json
import time
from collections import Counter


# current tweet number for this month
def current_twts():
    client = CouchDB('admin', 'data-miner!', url='http://172.26.133.205:5984', connect=True)
    cities = ["melbourne", "sydney", "adelaide", "canberra", "brisbane"]
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
    current_twts = {}
    number = 0
    for city in cities:
        citydb = client[city]
        djson = json.loads(date)
        if not djson['_id'] in citydb:
            citydb.create_document(djson)
        view = View(citydb['_design/date'], 'month_count')
        with view.custom_result(group=True) as results:
            for result in results:
                if result['key'] == time.strftime("%Y-%m", time.localtime()):
                    number = number + result['value']
    current_twts['number'] = number
    return current_twts


# total tweet number each year each city 
def total_twts():
    client = CouchDB('admin', 'data-miner!', url='http://172.26.133.205:5984', connect=True)
    cities = ["melbourne", "sydney", "adelaide", "canberra", "brisbane"]
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
    total_twts = {}
    for city in cities:
        citydb = client[city]
        djson = json.loads(date)
        if not djson['_id'] in citydb:
            citydb.create_document(djson)
        year_count = {}
        view = View(citydb['_design/date'], 'year_count')
        with view.custom_result(group=True) as results:
            for result in results:
                year_count[result['key']] = result['value']
        total_twts[city] = year_count
    return total_twts

    
# language distribution each city
def lang_dis():
    f = open('data/iso639.json', encoding="utf-8")
    iso639 = json.load(f)
    client = CouchDB('admin', 'data-miner!', url='http://172.26.133.205:5984', connect=True)
    cities = ["melbourne", "sydney", "adelaide", "canberra", "brisbane"]
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
    lang_dis = {}
    for city in cities:
        citydb = client[city]
        djson = json.loads(language)
        if not djson['_id'] in citydb:
            citydb.create_document(djson)
        lang_count = {}
        view = View(citydb['_design/language'], 'lang_count')
        with view.custom_result(group=True) as results:
            for result in results:
                if result['key'] != 'und' and result['key'] != 'en':
                    lang_count[result['key']] = result['value']
            lang_sorted = sorted(lang_count.items(),key = lambda x:x[1],reverse = True)
        for i in range(len(lang_sorted)):
            if i >= 10:
                lang_sorted[i] = ('others',lang_sorted[i][1])
            else:
                for j in iso639:
                    if lang_sorted[i][0] == j['639-1']:
                        lang_sorted[i] = (j['ISO language name'].split(", ")[0],lang_sorted[i][1])
                        
        lang_sorted_dict = dict(list(Counter(key for key, num in lang_sorted for idx in range(num)).items()))
        lang_dis[city] = lang_sorted_dict
    return lang_dis


# average sentiment score each year each city
def senti_score():
    client = CouchDB('admin', 'data-miner!', url='http://172.26.133.205:5984', connect=True)
    cities = ["melbourne", "sydney", "adelaide", "canberra", "brisbane"]
    sentiment = '''
    {
      "_id" : "_design/sentiment",
      "views" : {
        "senti_sum" : {
          "map" : "function(doc){emit(doc.date.substr(0,4),doc.sentiment)}",
          "reduce" : "_sum"
        },
        "en_count" : {
          "map" : "function(doc){if (doc.language === 'en') {emit(doc.date.substr(0,4))}}",
          "reduce" : "_count"
        }
      }
    }
    '''
    en_twts = {}
    for city in cities:
        citydb = client[city]
        djson = json.loads(sentiment)
        if not djson['_id'] in citydb:
            citydb.create_document(djson)
        en_count = {}
        view = View(citydb['_design/sentiment'], 'en_count')
        with view.custom_result(group=True) as results:
            for result in results:
                en_count[result['key']] = result['value']
        en_twts[city] = en_count
    senti_score = {}
    for city in cities:
        citydb = client[city]
        djson = json.loads(sentiment)
        if not djson['_id'] in citydb:
            citydb.create_document(djson)
        senti_avg = {}
        view = View(citydb['_design/sentiment'], 'senti_sum')
        with view.custom_result(group=True) as results:
            for result in results:
                senti_avg[result['key']] = result['value']/en_twts[city][result['key']]
        senti_score[city] = senti_avg
    return senti_score


# time(hour) distribution this month each city (UTC+10)
def time_dis():
    client = CouchDB('admin', 'data-miner!', url='http://172.26.133.205:5984', connect=True)
    cities = ["melbourne", "sydney", "adelaide", "canberra", "brisbane"]
    hour = '''
    {
      "_id" : "_design/hour",
      "views" : {
        "hour_count" : {
          "map" : "function(doc){if (doc.date.substr(0,7)==='2021-05') {emit(doc.time.substr(0,2))}}",
          "reduce" : "_count"
        }
      }
    }
    '''
    time_dis = {}
    for city in cities:
        citydb = client[city]
        djson = json.loads(hour)
        if not djson['_id'] in citydb:
            citydb.create_document(djson)
        hour_count = {}
        view = View(citydb['_design/hour'], 'hour_count')
        with view.custom_result(group=True) as results:
            for result in results:
                hour_count[(int(result['key'])+2)%24] = result['value']
        time_dis[city] = hour_count
    return time_dis


# top 30 used hashtags each year each city
def top_hashtags():
    client = CouchDB('admin', 'data-miner!', url='http://172.26.133.205:5984', connect=True)
    cities = ["melbourne", "sydney", "adelaide", "canberra", "brisbane"]
    years = ['2018','2019','2020','2021']
    top_hashtags = {}
    results = Result(client['hashtags'].all_docs, include_docs=True)
    for t in results:
        s = {}
        for year in years:
            s[year] = []
            for doc in t['doc'][year]:
                s[year].append({"name": doc[0], "value": doc[1]})
            # s[year] = dict(t['doc'][year])
        top_hashtags[t['doc']['_id']] = s
    return top_hashtags
