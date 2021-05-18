var mapData = [
    [],
    [],
    [],
    []
];

/*柱子Y名称*/
var categoryData = [];
var barData = [];
var langdis_data = [];
var timedis_data = [];

for (var key in geoCoordMap) {
    mapData[0].push({
        "year": '2018',
        "name": key,
        "value": city_2018[key],
    });
    mapData[1].push({
        "year": '2019',
        "name": key,
        "value": city_2019[key],
    });
    mapData[2].push({
        "year": '2020',
        "name": key,
        "value": city_2020[key],
    });
    mapData[3].push({
        "year": '2021',
        "name": key,
        "value": city_2021[key],
    });
    console.log(city_2021[key])
}

for (var i = 0; i < mapData.length; i++) {
    mapData[i].sort(function sortNumber(a, b) {
        return a.value - b.value
    });
    barData.push([]);
    categoryData.push([]);
    for (var j = 0; j < mapData[i].length; j++) {
        barData[i].push(mapData[i][j].value);
        categoryData[i].push(mapData[i][j].name);
    }
}

var convertData = function(data) {
    var res = [];
    for (var i = 0; i < data.length; i++) {
        var geoCoord = geoCoordMap[data[i].name];
        if (geoCoord) {
            res.push({
                name: data[i].name,
                value: geoCoord.concat(data[i].value)
            });
        }
    }
    return res;
};

// var piecolor=['#00ffff','#00cfff','#006ced','#ffe000','#ffa800','#ff5b00','#ff3000']
// for (var i = 0; i < keys.length; i++) {
//     var keyname = keys[i]; 
//     console.log(lang_data[i])
//     langdis_data.push({
//         name: keyname, //city
//         type: 'pie',
//         radius: ['50%', '70%'],
//         center: ['50%', '50%'],
//         color: ['#065aab', '#066eab', '#0682ab', '#0696ab', '#06a0ab','#06b4ab','#06c8ab','#06dcab','#06f0ab'],
//         data: lang_data[i], //.sort(function (a, b) { return a.value - b.value; }),
//         label: {
//             color: 'rgba(255, 255, 255, 0.3)',
//             normal: {
//                 Show: true, // ​​whether to display the label
//                 //// The location of the tag. The 'outside' is outside the pie slice and is connected to the corresponding sector by a visual guide. 'inside', 'inner' Same as 'inside', inside the pie slice. 'center' is at the center of the pie chart.
//                 position: 'left',
//                 // The content of the displayed label
//                 //a (series name), b (data item name), c (number), d (percentage)
//                 formatter: "{b}:{c}({d}%)", 
//                 emphasis: {
//                          //The label style displayed by the mouse on the ring
//                     show: true,
//                     textStyle: {
//                         fontSize: '10',
//                         fontWeight: 'bold'
//                     }
//                 }
//             }
//         },
//         labelLine: {
//             lineStyle: {
//                 // color: 'rgba(255, 255, 255, 0.3)'
//             },
//             smooth: 0.2,
//             length: 10,
//             length2: 20
//         },
//         itemStyle: {
//             // color: '#c23531',
//             shadowBlur: 200,
//             shadowColor: 'rgba(0, 0, 0, 0.5)',
//             label:{  
//                 show:true,
//                 position: 'outer',  
//                 formatter:'{d}%'  
//             }, 
//         },

//         animationType: 'scale',
//         animationEasing: 'elasticOut',
//         animationDelay: function (idx) {
//             return Math.random() * 200;
//         }
//     })
// }

// Language Distribution
for (var i = 0; i < keys.length; i++) {
    var keyname = keys[i]; 
    console.log(lang_data[i])
    langdis_data.push({
        name: keyname, //city
        type: 'bar',
        data: lang_data[i].sort(function (a, b) { return a.value - b.value; }),
        itemStyle: {
            normal: {
                color:'#2f89cf',
                opacity: 1,
                barBorderRadius: 5,
            }
        },
        large: true 
    })
}

// Time Distribution
for (var i = 0; i < keys.length; i++) {
    var keyname = keys[i]; 
    console.log(time_data[i])
    timedis_data.push({
        name: keyname, //city
        type: 'bar',
        data: time_data[i].sort(function (a, b) { return a.value - b.value; }),
        itemStyle: {
            normal: {
                color:'#2f89cf',
                opacity: 1,
                barBorderRadius: 5,
            }
        },
        large: true //.sort(function (a, b) { return a.value - b.value; }),
    })
}



// 饼状图配置
// var option = {
//     // backgroundColor: '#2c343c',
//     title: {
//         zlevel: 2,
//         // z:3,
//         text: pie_data[0]['name'],
//         top: 'middle',
//         left: 'center',
//         textStyle: {
//             color: '#fff',
//             fontSize: '14'
//         }
//     },
//     // legend: {
//     //     // The mode selected by the legend controls whether the display state of the series can be changed by clicking on the legend. The legend selection is turned on by default and can be set to false to close.
//     //     selectedMode: true, 
//     //     /* orient: 'vertical', */
//     //     /* x : 'right', //the legend is shown on the right
//     //     y: 'center', */ //The legend is centered above the vertical display
//     //     bottom:0,
//     //     itemWidth: 10, // the width of the legend mark
//     //     itemHeight: 10, //Graph height of the legend mark
//     //     // Data:['EN', 'CN', 'JP', 'KR', 'FR'],
//     //     textStyle: { // style of legend text
//     //     color: 'rgba(255,255,255,.5)',
//     //     // Color: '#A6A8B6', //text color
//     //     fontSize: 10 // text size
//     //     }
//     // },   		  
//     tooltip: {
//         trigger: 'item',
//         formatter: "{a} <br/>{b}: {c} ({d}%)",
//         textStyle: { // style of legend text
//                     Color:'#fff', //text color
//                     fontSize: 10 // text size
//         }
//     },
//     visualMap: {
//         show: false,
//         min: 0,
//         max: 1000000,
//         inRange: {
//             colorLightness: [0.5, 1]
//         }
//     },
//     series: [pie_data[0]]
// };

var lang_option = {
    title: {
        zlevel: 2,
        // z:3,
        text: langdis_data[0]['name'].toUpperCase(),
        top: '5%',
        left: 'center',
        textStyle: {
            color: '#fff',
            fontSize: '14'
        }
    },
    toolbox: {
        feature: {
            dataZoom: {
                yAxisIndex: false
            },
            saveAsImage: {
                pixelRatio: 2
            }
        }
    },
    tooltip: {
        trigger: 'item',
        formatter: "{a} <br/>{b}: {c}",
        textStyle: { // style of legend text
                    Color:'#fff', //text color
                    fontSize: 10 // text size
        }
    },
    grid: {
        left: '2%',
        top:'10px',
        right: '2%',
        bottom: '15%',
       containLabel: true
    },
    dataZoom: [{
        type: 'inside'
    }, {
        type: 'slider',
    }],
    xAxis: {
        type: 'category',
        data: Object.keys(vue.city_lang[keys[0]]),
        silent: false,
        splitLine: {
            show: false
        },
        splitArea: {
            show: false
        },
        axisLine: {
            show: true,
            lineStyle: {
                color: "rgba(255,255,255,.1)",
                width: 1,
                type: "solid"
            },
        },
        axisTick: {
            show: false,
        },
        axisLabel:  {
                interval: 5,
               // rotate:50,
                show: true,
                splitNumber: 5,
                textStyle: {
                     color: "rgba(255,255,255,.6)",
                    fontSize: '10',
                },
            },
    },
    yAxis: {
        axisLabel: {
            //formatter: '{value} %'
             show:true,
              textStyle: {
                      color: "rgba(255,255,255,.6)",
                     fontSize: '12',
                 },
         },
         axisTick: {
             show: false,
         },
         axisLine: {
             show: true,
             lineStyle: {
                 color: "rgba(255,255,255,.1)",
                 width: 1,
                 type: "solid"
             },
         },
         splitLine: {
             lineStyle: {
                color: "rgba(255,255,255,.1)",
             }
         },
        splitArea: {
            show: false
        }
    },
    series: [langdis_data[0]]
};

var time_option = {
    title: {
        zlevel: 2,
        // z:3,
        text: timedis_data[0]['name'].toUpperCase(),
        top: '5%',
        left: 'center',
        textStyle: {
            color: '#fff',
            fontSize: '14'
        }
    },
    toolbox: {
        feature: {
            dataZoom: {
                yAxisIndex: false
            },
            saveAsImage: {
                pixelRatio: 2
            }
        }
    },
    tooltip: {
        trigger: 'item',
        formatter: "{a} <br/>{b}: {c}",
        textStyle: { // style of legend text
                    Color:'#fff', //text color
                    fontSize: 10 // text size
        }
    },
    grid: {
        left: '2%',
        top:'10px',
        right: '2%',
        bottom: '15%',
       containLabel: true
    },
    dataZoom: [{
        type: 'inside'
    }, {
        type: 'slider',
    }],
    xAxis: {
        type: 'category',
        data: Object.keys(vue.city_time_dis[keys[0]]),
        silent: false,
        splitLine: {
            show: false
        },
        splitArea: {
            show: false
        },
        axisLine: {
            show: true,
            lineStyle: {
                color: "rgba(255,255,255,.1)",
                width: 1,
                type: "solid"
            },
        },
        axisTick: {
            show: false,
        },
        axisLabel:  {
                interval: 5,
               // rotate:50,
                show: true,
                splitNumber: 5,
                textStyle: {
                     color: "rgba(255,255,255,.6)",
                    fontSize: '10',
                },
            },
    },
    yAxis: {
        axisLabel: {
            //formatter: '{value} %'
             show:true,
              textStyle: {
                      color: "rgba(255,255,255,.6)",
                     fontSize: '12',
                 },
         },
         axisTick: {
             show: false,
         },
         axisLine: {
             show: true,
             lineStyle: {
                 color: "rgba(255,255,255,.1)",
                 width: 1,
                 type: "solid"
             },
         },
         splitLine: {
             lineStyle: {
                color: "rgba(255,255,255,.1)",
             }
         },
        splitArea: {
            show: false
        }
    },
    series: [timedis_data[0]]
};