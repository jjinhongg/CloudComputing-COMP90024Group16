import twint
import json
import pandas as pd
import twint
import schedule
import time

def obtain_cities():
    cities = ["Melbourne", "Sydney", 
              "Adelaide", "Canberra", 
              "Brisbane"]
    return cities

def obtain_coordinates(name):
    cities = {"Melbourne": (-37.8136, 144.9631), "Sydney": (-33.8688, 151.2093), 
              "Adelaide": (-34.9285, 138.6007), "Canberra": (-35.2809, 149.1300), 
              "Brisbane": (-27.4705, 153.0260)}
    return cities[name]

def tweetCrawling(location, coordinate, range):
    outputf = '.'.join([location, "json"])
    print(outputf)
    c = twintCongig(coordinate, range, outputf)
    twint.run.Search(c)
    
def twintCongig(coordinate, range, outputf):
    geo = ",".join([str(coordinate[0]), str(coordinate[1]), range])
    c = twint.Config()
    c.Geo = geo
    c.Since = "2019-01-01"
    c.Until = "2019-12-31"
    c.Limit = 500
    c.Output = outputf
    c.Store_json = True
    return c

for city in obtain_cities(): 
    tweetCrawling(city, obtain_coordinates(city), "10km")

# def jobone():
#     # Configure
#     c = twint.Config()
#     # c.Search = "covid"
#     # c.Lang = "en"
#     c.Geo = "-37.810, 144.970, 1km"
#     c.Limit = 100
#     c.Since = "2021-1-1"
#     # c.Location = True
#     # c.Custom = ["id", "user_id", "username", "date", "time", "name", "tweet", "language", "hashtags"]
#     c.Output = "./test2.json"
#     c.Store_json = True

#     # Run
#     twint.run.Search(c)

# # run once when you start the program
# jobone()
# schedule.every().minute.do(jobone)

# while True:
#     schedule.run_pending()
#     time.sleep(1)

# import json

# data = []
# with open('./test.json') as f:
#     for line in f:
#         data.append(json.loads(line))
# print(data)

# def save_or_load_data(save_data=True):
#     '''
#     保存当前爬取的1000条推文，到couchdb,json格式
#     如果save等于true，保存数据，要么读取数据
#     :return: None
#     '''

#     couch = couchdb.Server('http://127.0.0.1:5984/')
#     db = None
#     db_name = 'a2'
#     try:
#         db = couch[db_name]
#     except:
#         db = couch.create(db_name)
#     if save_data:
#         df = pd.read_json("file.json", orient='records')
#         doc = json.loads(df.to_json(orient='table'))
#         doc['_id'] = 'db_doc'
#         db.save(doc)
#     else:
#         with open("./current.json", 'w') as json_file:
#             json.dump(db['db_doc'], json_file, ensure_ascii=False)
