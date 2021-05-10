from cloudant.client import CouchDB
from cloudant.view import View
import json
from collections import Counter

client = CouchDB('admin', 'data-miner!', url='http://172.26.133.205:5984', connect=True)

cities = ["melbourne", "sydney", "adelaide", "canberra", "brisbane"]
city = cities[0]
citydb = client[city]
ddoc = citydb['_design/mydesign']

# total tweets number
twt_count = citydb.all_docs()['total_rows'] - 1

# count tweets for each language
view1 = View(ddoc, 'lang_count')
lang_count = {}
with view1.custom_result(group=True) as results1:
    for result in results1:
        lang_count[result['key']] = result['value']

# gather hashtags
view2 = View(ddoc, 'all_hashtags')
all_hashtags = []
for result in view2.result:
    all_hashtags = all_hashtags + result['key']
hashtags_count = dict(Counter(all_hashtags))
hashtags_sorted = sorted(hashtags_count.items(),key = lambda x:x[1],reverse = True)

# count tweets for each hour
view3 = View(ddoc, 'time_count')
time_count = {}
with view3.custom_result(group=True) as results3:
    for result in results3:
        time_count[(int(result['key'])+2)%24] = result['value']

print(lang_count)

print(hashtags_sorted[0:30])

print(time_count)