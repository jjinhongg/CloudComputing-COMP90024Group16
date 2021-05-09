from flask import Flask
from flask import render_template
import time
import utils
import couchdb
app = Flask(__name__,
            static_url_path='/static', 
            static_folder='static',
            template_folder='templates')

@app.route('/')
def hello_world():
    return render_template('main.html')

@app.route('/test')
def template_test():
    # return render_template('template_assignemnt2.html')
    return render_template('test_1.html')

#显示时间
@app.route("/time")
def gettime():
    return time.strftime("%Y{}%m{}%d %X").format('-','-')

#显示当前处理推特数量
@app.route("/totalTweeters")
def get_all_number():
    number = utils.count_all_tweet()
    return '一共'+str(number)+'推特数量'

#地图散点图显示推特分布
@app.route("/mapshow")
def get_map_info():
    return '123'

#类似于弹幕，滚动推特文本显示
@app.route("/tweetShow")
def get_tweeters():
    return utils.get_tweeters()

#统计分析结果显示
@app.route("/analysisResult")
def get_result_info():
    return '123'

#推特词云显示
@app.route('/wordworld')
def get_hot_words():
    return ['123','456']

#存储数据到本地
@app.route('/testinsert')
def insert_data():
    couch = couchdb.Server('http://admin:admin@127.0.0.1:5984/')
    db = None
    dbName = 'test'
    try:
        db = couch[dbName]
    except:
        db = couch.create(dbName)

    doc = {'foo': 'bar'}
    db.save(doc)
    return 'success'

#读取数据 根据指定database 和 key
@app.route('/testget/<database>')
def get_data(database):
    couch = couchdb.Server('http://admin:admin@127.0.0.1:5984/')
    db = couch[database]
    for id in db:
        print(db[id])
    return 'success'

#删除数据库
@app.route('/testdel/<database>')
def del_database(database):
    couch = couchdb.Server('http://admin:admin@127.0.0.1:5984/')
    try:
        couch.delete(database)
        return 'success'
    except:
        return 'failed'


if __name__ == '__main__':
    app.run(debug=True)
