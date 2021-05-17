var city_2018 = {}, city_2019 = {}, city_2020 = {}, city_2021 = {};
var lang_data = [];

var year = ["2018","2019", "2020", "2021"];
//geoCoordMap把所有可能出现的城市加到数组里面
var geoCoordMap = {
    'adelaide': [138.6007, -34.9285],
    'brisbane': [153.0260, -27.4705],
    "canberra": [149.1300, -35.2809],
    "melbourne": [144.9631, -37.8136],
    "sydney": [151.2093, -33.8688],
};
var keys = Object.keys( geoCoordMap );
// console.log(keys)


setTimeout(function(){
    //2018年数据
  city_2018['adelaide'] = vue.$data.city_tweets.adelaide['2018']
  city_2018['brisbane'] =  vue.$data.city_tweets.brisbane['2018']
  city_2018["canberra"] = vue.$data.city_tweets.canberra['2018']
  city_2018["melbourne"] = vue.$data.city_tweets.melbourne['2018']
  city_2018["sydney"] = vue.$data.city_tweets.sydney['2018']
    //2019年数据
  city_2019['adelaide'] = vue.$data.city_tweets.adelaide['2019']
  city_2019['brisbane'] =  vue.$data.city_tweets.brisbane['2019']
  city_2019["canberra"] = vue.$data.city_tweets.canberra['2019']
  city_2019["melbourne"] = vue.$data.city_tweets.melbourne['2019']
  city_2019["sydney"] = vue.$data.city_tweets.sydney['2019']
    //2020年数据
  city_2020['adelaide'] = vue.$data.city_tweets.adelaide['2020']
  city_2020['brisbane'] =  vue.$data.city_tweets.brisbane['2020']
  city_2020["canberra"] = vue.$data.city_tweets.canberra['2020']
  city_2020["melbourne"] = vue.$data.city_tweets.melbourne['2020']
  city_2020["sydney"] = vue.$data.city_tweets.sydney['2020']
    //2021年数据
  city_2021['adelaide'] = vue.$data.city_tweets.adelaide['2021']
  city_2021['brisbane'] =  vue.$data.city_tweets.brisbane['2021']
  city_2021["canberra"] = vue.$data.city_tweets.canberra['2021']
  city_2021["melbourne"] = vue.$data.city_tweets.melbourne['2021']
  city_2021["sydney"] = vue.$data.city_tweets.sydney['2021']
  // console.log(Object.keys( vue.city_tweets ))

  //Initialise language data for each city
  for (loc in geoCoordMap){
    window[loc+'_lang'] = []
    for (var lang in vue.city_lang[loc]){
        window[loc+'_lang'].push({"name": lang, "value": vue.city_lang[loc][lang]})
        }
    
    lang_data.push(window[loc+'_lang'])
    }
},10000);

setTimeout(function(){
    console.log(adelaide_lang)
    console.log(lang_data)
  },15000);

