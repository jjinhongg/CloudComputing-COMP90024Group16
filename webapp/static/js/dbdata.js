setTimeout(function(){
    console.log(vue.city_tweets)
    // console.log(Object.keys( vue.city_tweets ))
  },4000);

// setTimeout(function(){
//     console.log(city_tweets)
//     // console.log(Object.keys( vue.city_tweets ))
//   },4000);

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

//2018年数据
var city_2018 = {
    'adelaide': vue.city_tweets.adelaide['2018'],
    'brisbane': vue.city_tweets.brisbane['2018'],
    "canberra": vue.city_tweets.canberra['2018'],
    "melbourne": vue.city_tweets.melbourne['2018'],
    "sydney": vue.city_tweets.sydney['2018'],
};
//2019年数据
var city_2019 = {
    'adelaide': vue.city_tweets.adelaide['2019'],
    'brisbane': vue.city_tweets.brisbane['2019'],
    "canberra": vue.city_tweets.canberra['2019'],
    "melbourne": vue.city_tweets.melbourne['2019'],
    "sydney": vue.city_tweets.sydney['2019'],
};
//2020年数据
var city_2020 = {
    'adelaide': vue.city_tweets.adelaide['2020'],
    'brisbane': vue.city_tweets.brisbane['2020'],
    "canberra": vue.city_tweets.canberra['2020'],
    "melbourne": vue.city_tweets.melbourne['2020'],
    "sydney": vue.city_tweets.sydney['2020'],
};
//2021年数据
var city_2021 = {
    'adelaide': vue.city_tweets.adelaide['2021'],
    'brisbane': vue.city_tweets.brisbane['2021'],
    "canberra": vue.city_tweets.canberra['2021'],
    "melbourne": vue.city_tweets.melbourne['2021'],
    "sydney": vue.city_tweets.sydney['2021'],
};

for (loc in geoCoordMap){
    window[loc+'_lang'] = []
    for (lang in Object.keys(vue.city_lang.loc)){
        window[loc+'_lang'].push({"name": lang, "value": vue.city.loc[lang]})
    }
        
}
console.log(adelaide_lang)