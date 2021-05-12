from flask import Flask
from flask import render_template
import time
import utils
import data_analysis
from cloudant.client import Cloudant
app = Flask(__name__)

app.jinja_env.auto_reload = True
app.config['TEMPLATES_AUTO_RELOAD'] = True

@app.route('/123')
def hello_world():
   return render_template('main.html')

@app.route('/')
def template_test():
    return render_template('template_assignemnt2.html')

#显示时间
@app.route("/time")
def gettime():
    return time.strftime("%Y{}%m{}%d %X").format('-','-')

#显示当前处理推特数量
@app.route("/totalTweeters")
def get_all_number():
    current_twts = data_analysis.current_twts()
    return current_twts

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



if __name__ == '__main__':
    app.run()
