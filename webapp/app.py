from flask import Flask
from flask import render_template, jsonify
import time
import utils
import data_analysis
from cloudant.client import CouchDB
from cloudant.client import Cloudant
app = Flask(__name__)

app.jinja_env.auto_reload = True
app.config['TEMPLATES_AUTO_RELOAD'] = True
# client = CouchDB('admin', 'data-miner!', url='http://172.26.133.205:5984', connect=True)

@app.route('/')
def template_test():
    return render_template('template_assignemnt2.html')

#显示时间
@app.route("/time")
def gettime():
    return time.strftime("%Y{}%m{}%d %X").format('-','-')

#显示当前处理推特数量
@app.route("/totaltweeters")
def get_current_twts():
    currenttwts = data_analysis.current_twts()
    return jsonify(currenttwts)

# total tweet number each year each city
@app.route("/tweetperyearcity")
def get_total_twts():
    totaltwt = data_analysis.total_twts()
    return jsonify(totaltwt)

# language distribution each city
@app.route("/languagedistribution")
def get_lang_dis():
    langdis = data_analysis.lang_dis()
    return jsonify(langdis)

# average sentiment score each year each city
@app.route("/sentiment")
def get_sentiment():
    sentiscore = data_analysis.senti_score()
    return jsonify(sentiscore)

# time(hour) distribution this month each city (UTC+10)
@app.route("/timedistribution")
def get_timedistribution():
    timedis = data_analysis.time_dis()
    return jsonify(timedis)


# top 30 used hashtags this year each city
@app.route("/tophashtags")
def get_tophashtags():
    tophashtags = data_analysis.top_hashtags()
    return jsonify(tophashtags)

if __name__ == '__main__':
    app.run()
