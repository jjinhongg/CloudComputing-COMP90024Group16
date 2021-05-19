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
client = CouchDB('admin', 'data-miner!', url='http://172.26.133.205:5984', connect=True)

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
    currenttwts = data_analysis.current_twts(client)
    return jsonify(currenttwts)

# total tweet number each year each city
@app.route("/tweetperyearcity")
def get_total_twts():
    totaltwt = data_analysis.total_twts(client)
    return jsonify(totaltwt)

# language distribution each city
@app.route("/languagedistribution")
def get_lang_dis():
    langdis = data_analysis.lang_dis(client)
    return jsonify(langdis)

# average sentiment score each year each city
@app.route("/sentiment")
def get_sentiment():
    sentiscore = data_analysis.senti_score(client)
    return jsonify(sentiscore)

# time(hour) distribution this month each city (UTC+10)
@app.route("/timedistribution")
def get_timedistribution():
    timedis = data_analysis.time_dis(client)
    return jsonify(timedis)


# top 30 used hashtags this year each city
@app.route("/tophashtags")
def get_tophashtags():
    cities = ["adelaide", "brisbane", "canberra", "melbourne", "sydney"]
    tophashtags = {'melbourne': {'auspol': 2890,
    'melbourne': 1740,
    'victraffic': 1501,
    'trx': 1274,
    'whatshappeninginmyanmar': 1161,
    'iheartawards': 1150,
    'afltigerscats': 750,
    'australia': 721,
    'tron': 688,
    'afl': 571,
    'bbau': 567,
    'masterchefau': 561,
    'afldonsblues': 546,
    'covid19': 543,
    'tigraygenocide': 472,
    'nft': 467,
    'wynonnaearp': 458,
    'springst': 431,
    'bringwynonnahome': 429,
    'bestmusicvideo': 414,
    'funkykidsradio': 405,
    'music4kids': 405,
    'thebool': 401,
    'prayfortigray': 374,
    'e': 345,
    'safemoon': 340,
    'a': 334,
    's': 324,
    'maythe4thbewithyou': 323,
    'nftcollector': 322},
    'sydney': {'auspol': 2491,
    'sydney': 2294,
    'whatshappeninginmyanmar': 1554,
    'photography': 1273,
    'australia': 1033,
    'kaye_menner': 941,
    'masterchefau': 797,
    'safemoon': 793,
    'iheartawards': 757,
    'nrl': 724,
    'covid19': 553,
    'asx': 482,
    'btc': 472,
    'bbau': 463,
    'sydneyderby': 439,
    'art': 439,
    'quote': 419,
    'bestfanarmy': 407,
    'nrleelsroosters': 404,
    'nswpol': 392,
    '7news': 385,
    'crypto': 382,
    'football': 382,
    'launchzone': 366,
    'sydneywritersfestival': 362,
    'haarlemaustralia': 343,
    'sanditon': 341,
    'ausbiz': 337,
    'e': 325,
    'bitcoin': 323},
    'adelaide': {'adelaide': 1525,
    'auspol': 1158,
    'weflyasone': 590,
    'southaustralia': 531,
    'australia': 516,
    'adlww': 511,
    'adlfest': 500,
    '7news': 428,
    '9news': 310,
    'fashion': 217,
    'afl': 196,
    'whatshappeninginmyanmar': 187,
    'asm21mel': 185,
    'saparli': 183,
    'enoughisenough': 169,
    'nowplaying': 168,
    'sarockradio': 154,
    'covid19': 150,
    'southstart2021': 150,
    'art': 144,
    'style': 129,
    'sirsavapisaajopitaji': 122,
    'e': 115,
    'weareportadelaide': 107,
    'a': 107,
    'hottest100': 105,
    'adlfringe': 103,
    'bbl10': 101,
    'afllionspower': 98,
    'thesimpsons100': 97},
    'canberra': {'auspol': 1729,
    'canberra': 606,
    'thedrum': 456,
    'covid19': 318,
    'nrl': 258,
    '路德時評摘要': 227,
    'australia': 187,
    'march4justice': 166,
    'upthemilk': 165,
    'insiders': 158,
    'cbr': 131,
    'mafs': 130,
    'qanda': 129,
    'india': 121,
    'cyberdigest': 119,
    'brumbiesfamily': 118,
    'superrugbyau': 115,
    'mafsau': 113,
    'tasvotes': 102,
    'jointhepipeline': 99,
    'afl': 98,
    'enoughisenough': 94,
    'bruvfor': 94,
    'weareraiders': 86,
    'sydneywritersfestival': 83,
    'cats': 76,
    'catsoftwitter': 74,
    'china': 69,
    '7news': 68,
    'scottyfrommarketing': 67},
    'brisbane': {'auspol': 2698,
    'brisbane': 966,
    'whatshappeninginmyanmar': 802,
    'covid19': 477,
    'australia': 436,
    'writer': 426,
    'author': 417,
    'blog': 414,
    'scummo': 410,
    'scottydoesnothing': 409,
    'blogging': 400,
    'iheartawards': 398,
    'bambam': 395,
    'retweet': 390,
    'rt': 389,
    'nowplaying': 389,
    'lnpcorruptionparty': 388,
    'writing': 364,
    'bestfanarmy': 363,
    'federalicac': 361,
    'nrl': 355,
    'louies': 355,
    'liarfromtheshire': 349,
    'แบมแบม': 346,
    'quote': 345,
    'blogger': 336,
    'ausvind': 324,
    'worstpmever': 320,
    'creativity': 304,
    'authorlife': 267}}

    # hashtags_data = []
    # for city in cities:
    #     tags = []
    #     for loc in tophashtags[city]:
    #         temp_dict = {}
    #         temp_dict['x'] = loc
    #         temp_dict['value'] = tophashtags[city][loc]
    #         # temp_dict['category'] = city
    #         tags.append(temp_dict)
    #     hashtags_data.append(tags)

    return jsonify(tophashtags)

if __name__ == '__main__':
    app.run()
