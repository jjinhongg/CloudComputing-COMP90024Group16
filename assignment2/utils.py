
import random
import json
import pandas as pd
import couchdb
import twint
import schedule
import time
import os

def update_l1_data():
    pass

def run_spider():
    '''
    定时爬取墨尔本地区30km的全有推文，限制1000条
    :return: None
    '''

    def jobone():
        print("Fetching Tweets")
        c = twint.Config()
        c.Geo = "-37.8136,144.963,30km"
        # choose beginning time (narrow results)
        # set limit on total tweets
        c.Limit = 1000
        # no idea, but makes the csv format properly
        c.Custom = ["date", "time", "username", "tweet", "link", "likes", "retweets", "replies", "mentions", "hashtags"]
        # change the name of the csv file
        c.Output = "file.json"
        twint.run.Search(c)
    # run once when you start the program
    jobone()
    schedule.every().hour.do(jobone)

    while True:
        schedule.run_pending()
        time.sleep(1)

def save_into_couchdb():
    '''
    保存当前爬取的1000条推文，到couchdb,json格式
    :return: None
    '''

    couch = couchdb.Server('http://127.0.0.1:5984/')
    db = None
    db_name = 'a2'
    try:
        db = couch[db_name]
    except:
        db = couch.create(db_name)
    ##读取文档并插入到数据库：
    df = pd.read_json("file.json", orient='records')
    doc = json.loads(df.to_json(orient='table'))
    doc['_id'] = 'db_doc'
    db.save(doc)

