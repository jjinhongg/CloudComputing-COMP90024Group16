var colors = [
    ["#1DE9B6", "#F46E36", "#04B9FF", "#5DBD32", "#FFC809", "#FB95D5", "#BDA29A", "#6E7074", "#546570", "#C4CCD3"],
    ["#37A2DA", "#67E0E3", "#32C5E9", "#9FE6B8", "#FFDB5C", "#FF9F7F", "#FB7293", "#E062AE", "#E690D1", "#E7BCF3", "#9D96F5", "#8378EA", "#8378EA"],
    ["#DD6B66", "#759AA0", "#E69D87", "#8DC1A9", "#EA7E53", "#EEDD78", "#73A373", "#73B9BC", "#7289AB", "#91CA8C", "#F49F42"],
];
var colorIndex = 0;


setTimeout(function(){
$(function () {
    map();
    function map() {
        var timeChart = echarts.init(document.getElementById('echart1')); //初始化语言分布图
        var langChart = echarts.init(document.getElementById('echart2')); //初始化语言分布图
        var sentChart = echarts.init(document.getElementById('echart4')); //初始化语言分布图
        var wordCloud = echarts.init(document.getElementById('echart5')); //初始化语言分布图
        // 基于准备好的dom，初始化echarts实例
        var myChart = echarts.init(document.getElementById('map_1'));

        //--------------------------- Variables Initialisation ---------------------------\\

        console.log(hashtags_data)
        
        var mapData = [
            [],
            [],
            [],
            []
        ];
        var categoryData = [];
        var barData = [];
        var langdis_data = [];
        var timedis_data = [];
        var sentdis_data = [];
        var tophashtags_data = [];
        
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
                categoryData[i].push(mapData[i][j].name.toUpperCase());
            }
        }
        
        var convertData = function(data) {
            var res = [];
            for (var i = 0; i < data.length; i++) {
                var geoCoord = geoCoordMap[data[i].name];
                if (geoCoord) {
                    res.push({
                        name: data[i].name.toUpperCase(),
                        value: geoCoord.concat(data[i].value)
                    });
                }
            }
            return res;
        };
        
        // var piecolor=['#00ffff','#00cfff','#006ced','#ffe000','#ffa800','#ff5b00','#ff3000']
        // Language Distribution Pie Chart
        for (var i = 0; i < keys.length; i++) {
            var keyname = keys[i].toUpperCase(); 
            console.log(lang_data[i])
            langdis_data.push({
                name: keyname, //city
                type: 'pie',
                hoverAnimation: 'false',
                radius: ['40%', '60%'],
                center: ['50%', '50%'],
                // color: ['#065aab', '#066eab', '#0682ab', '#0696ab', '#06a0ab','#06b4ab','#06c8ab','#06dcab','#06f0ab'],
                data: lang_data[i], //.sort(function (a, b) { return a.value - b.value; }),
                emphasis: {
                    itemStyle: {
                        shadowBlur: 10,
                        shadowOffsetX: 0,
                        shadowColor: 'rgba(0, 0, 0, 0.5)'
                    }
                },
                label:{
                    color: 'rgba(255, 255, 255, 0.9)'
                },
                // label: {
                //     color: 'rgba(255, 255, 255, 0.3)',
                //     overflow: 'truncate',
                //     edgeDistance: '25%',
                //     bleedMargin: 10,
                //     distanceToLabelLine: 5,
                //     normal: {
                //         Show: true, // ​​whether to display the label
                //         //// The location of the tag. The 'outside' is outside the pie slice and is connected to the corresponding sector by a visual guide. 'inside', 'inner' Same as 'inside', inside the pie slice. 'center' is at the center of the pie chart.
                //         position: 'left',
                //         // The content of the displayed label
                //         //a (series name), b (data item name), c (number), d (percentage)
                //         formatter: "{b}:{c}({d}%)", 
                //         emphasis: {
                //                  //The label style displayed by the mouse on the ring
                //             show: true,
                //             textStyle: {
                //                 fontSize: '6',
                //                 fontWeight: 'bold'
                //             }
                //         }
                //     }
                // },
                labelLine: {
                    lineStyle: {
                        // color: 'rgba(255, 255, 255, 0.3)'
                    },
                    show: true,
                    smooth: 0.2,
                    length: 15,
                    length2: 30,
                    minTurnAngle: 0,
                    maxSurfaceAngle: 0
                },
                itemStyle: {
                    color: '#00abff',
                    // normal: {
                    //     borderWidth: 1,
                    //     borderColor: '#ff9900',
                    // },
                    shadowBlur: 200,
                    shadowColor: 'rgba(0, 0, 0, 0.5)',
                    // label:{  
                    //     show:true,
                    //     position: 'outer',  
                    //     formatter:'{d}%'  
                    // }, 
                },
                animationType: 'scale',
                animationEasing: 'elasticOut',
                animationDelay: function (idx) {
                    return Math.random() * 200;
                }
            })
        }
        
        // Language Distribution
        // for (var i = 0; i < keys.length; i++) {
        //     var keyname = keys[i]; 
        //     console.log(lang_data[i])
        //     langdis_data.push({
        //         name: keyname, //city
        //         type: 'bar',
        //         data: lang_data[i], //.sort(function (a, b) { return a.value - b.value; }),
        //         itemStyle: {
        //             normal: {
        //                 color:'#2f89cf',
        //                 opacity: 1,
        //                 barBorderRadius: 5,
        //             }
        //         },
        //         large: true 
        //     })
        // }
        
        // Time Distribution
        for (var i = 0; i < keys.length; i++) {
            var keyname = keys[i].toUpperCase(); 
            console.log(time_data[i])
            timedis_data.push(
                {
                    name: keyname,
                    type: 'line',
                    smooth: true,
                    symbol: 'circle',
                    symbolSize: 5,
                    showSymbol: false,
                    lineStyle: {
                        
                        normal: {
                            color: '#0184d5',
                            width: 2
                        }
                    },
                    areaStyle: {
                        normal: {
                            color: new echarts.graphic.LinearGradient(0, 0, 0, 1, [{
                                offset: 0,
                                color: 'rgba(1, 132, 213, 0.4)'
                            }, {
                                offset: 0.8,
                                color: 'rgba(1, 132, 213, 0.1)'
                            }], false),
                            shadowColor: 'rgba(0, 0, 0, 0.1)',
                        }
                    },
                    itemStyle: {
                        normal: {
                            color: '#0184d5',
                            borderColor: 'rgba(221, 220, 107, .1)',
                            borderWidth: 12
                        }
                    },
                    markArea: {
                        label:{
                            color: 'rgba(255, 255, 255, 0.9)',
                        },
                        itemStyle: {
                            color: 'rgba(255, 173, 177, 0.4)'
                        },
                        data: [ [{
                            name: 'Morning Peak',
                            xAxis: '7'
                        }, {
                            xAxis: '10'
                        }], [{
                            name: 'Evening Peak',
                            xAxis: '17'
                        }, {
                            xAxis: '21'
                        }] ]
                    },
                    data: time_data[i]
            
                })
        }

        // Sentiment Distribution
        for (var i = 0; i < keys.length; i++) {
            var keyname = keys[i].toUpperCase(); 
            console.log(sent_data[i])
            sentdis_data.push({
                name: keyname, //city
                type: 'line',
                smooth: true,
                symbol: 'circle',
                symbolSize: 5,
                showSymbol: false,
                data: sent_data[i], //.sort(function (a, b) { return a.value - b.value; }),
            })
        }        
        
        // WordCloud
        for (var i = 0; i < keys.length; i++) {
            var keyname = keys[i].toUpperCase(); 
            console.log(hashtags_data[i])
            tophashtags_data.push({
                    name: keyname,
                    type: 'wordCloud',
                    sizeRange: [30, 80],//文字范围
                    //文本旋转范围，文本将通过rotationStep45在[-90,90]范围内随机旋转
                    rotationRange: [-45, 90],
                    rotationStep: 45,
                    textRotation: [0, 45, 90, -45],
                    //形状
                    shape: 'circle',
                    // Global text style
                    textStyle: {
                        fontFamily: 'sans-serif',
                        fontWeight: 'bold',
                        // Color can be a callback function or a color string
                        color: function () {
                            // Random color
                            return 'rgb(' + [
                                Math.round(Math.random() * 180),
                                Math.round(Math.random() * 180),
                                Math.round(Math.random() * 180)
                            ].join(',') + ')';
                        }
                    },
                    //悬停上去的字体的阴影设置
                    emphasis: {
                        focus: 'self',
            
                        textStyle: {
                            shadowBlur: 10,
                            shadowColor: '#333'
                        }
                    },
                    data: hashtags_data[i]
                })
            }
        
        // 饼状图配置
        var lang_option = {
            // backgroundColor: '#2c343c',
            title: {
                zlevel: 2,
                // z:3,
                text: langdis_data[0]['name'],
                top: 'middle',
                left: 'center',
                textStyle: {
                    color: '#fff',
                    fontSize: '14'
                }
            },
            // legend: {
            //     // The mode selected by the legend controls whether the display state of the series can be changed by clicking on the legend. The legend selection is turned on by default and can be set to false to close.
            //     selectedMode: true, 
            //     /* orient: 'vertical', */
            //     /* x : 'right', //the legend is shown on the right
            //     y: 'center', */ //The legend is centered above the vertical display
            //     bottom:0,
            //     itemWidth: 10, // the width of the legend mark
            //     itemHeight: 10, //Graph height of the legend mark
            //     // Data:['EN', 'CN', 'JP', 'KR', 'FR'],
            //     textStyle: { // style of legend text
            //     color: 'rgba(255,255,255,.5)',
            //     // Color: '#A6A8B6', //text color
            //     fontSize: 10 // text size
            //     }
            // },   		  
            tooltip: {
                trigger: 'item',
                formatter: "{a} <br/>{b}: {c} ({d}%)",
                textStyle: { // style of legend text
                            Color:'#fff', //text color
                            fontSize: 12 // text size
                }
            },
            visualMap: {
                show: false,
                min: Math.min(...Object.values(vue.city_lang[keys[0]])),
                max: Math.max(...Object.values(vue.city_lang[keys[0]])),
                inRange: {
                    colorLightness: [0.2, 0.5]
                }
            },
            series: [langdis_data[0]]
        };
        
        // var lang_option = {
        //     title: {
        //         zlevel: 2,
        //         // z:3,
        //         text: langdis_data[0]['name'].toUpperCase(),
        //         // top: '2%',
        //         left: 'center',
        //         textStyle: {
        //             color: '#fff',
        //             fontSize: '14'
        //         }
        //     },
        //     toolbox: {
        //         feature: {
        //             dataZoom: {
        //                 yAxisIndex: false
        //             },
        //             saveAsImage: {
        //                 pixelRatio: 2
        //             }
        //         }
        //     },
        //     tooltip: {
        //         trigger: 'item',
        //         formatter: "{a} <br/>{b}: {c}",
        //         textStyle: { // style of legend text
        //                     Color:'#fff', //text color
        //                     fontSize: 12 // text size
        //         }
        //     },
        //     grid: {
        //         left: '2%',
        //         top:'20px',
        //         right: '2%',
        //         bottom: '15%',
        //        containLabel: true
        //     },
        //     dataZoom: [{
        //         type: 'inside'
        //     }, {
        //         type: 'slider',
        //     }],
        //     xAxis: {
        //         type: 'category',
        //         data: Object.keys(vue.city_lang[keys[0]]),
        //         silent: false,
        //         splitLine: {
        //             show: false 
        //         },
        //         splitArea: {
        //             show: false
        //         },
        //         axisLine: {
        //             show: true,
        //             lineStyle: {
        //                 color: "rgba(255,255,255,.1)",
        //                 width: 1,
        //                 type: "solid"
        //             },
        //         },
        //         axisTick: {
        //             show: false,
        //         },
        //         axisLabel:  {
        //                 interval: 5,
        //                // rotate:50,
        //                 show: true,
        //                 splitNumber: 5,
        //                 textStyle: {
        //                      color: "rgba(255,255,255,.6)",
        //                     fontSize: '10',
        //                 },
        //             },
        //     },
        //     yAxis: {
        //         axisLabel: {
        //             //formatter: '{value} %'
        //              show:true,
        //               textStyle: {
        //                       color: "rgba(255,255,255,.6)",
        //                      fontSize: '12',
        //                  },
        //          },
        //          axisTick: {
        //              show: false,
        //          },
        //          axisLine: {
        //              show: true,
        //              lineStyle: {
        //                  color: "rgba(255,255,255,.1)",
        //                  width: 1,
        //                  type: "solid"
        //              },
        //          },
        //          splitLine: {
        //              lineStyle: {
        //                 color: "rgba(255,255,255,.1)",
        //              }
        //          },
        //         splitArea: {
        //             show: false
        //         }
        //     },
        //     series: [langdis_data[0]]
        // };
        
        var time_option = {
            title: {
                zlevel: 2,
                // z:3,
                text: timedis_data[0]['name'].toUpperCase(),
                // top: '2%',
                left: 'center',
                top: 'center',
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
                trigger: 'axis',
                axisPointer: {
                    lineStyle: {
                        color: '#dddc6b'
                    }
                },
                // formatter: "{a} <br/>{b}: {c}",
                textStyle: { // style of legend text
                            Color:'#fff', //text color
                            fontSize: 12 // text size
                }
            },
            grid: {
                left: '2%',
                top:'20px',
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
                        interval: 0,
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
            visualMap: {
                show: false,
                dimension: 0,
                pieces: [{
                    lte: 7,
                    color: '#0184d5'
                }, {
                    gt: 7,
                    lte: 10,
                    color: 'red'
                }, {
                    gt: 10,
                    lte: 17,
                    color: '#0184d5'
                }, {
                    gt: 17,
                    lte: 21,
                    color: 'red'
                }, {
                    gt: 17,
                    color: '#0184d5'
                }]
            },
            series: [timedis_data[0]]
        };

        var sent_option = {
            // title: {
            //     zlevel: 2,
            //     // z:3,
            //     // text: sentdis_data[0]['name'].toUpperCase(),
            //     // top: '2%',
            //     left: 'center',
            //     textStyle: {
            //         color: '#fff',
            //         fontSize: '14'
            //     }
            // },
            toolbox: {
                feature: {
                    // dataZoom: {
                    //     yAxisIndex: false
                    // },
                    saveAsImage: {
                        pixelRatio: 2
                    }
                }
            },
            tooltip: {
                trigger: 'axis',
                // axisPointer: {
                //     lineStyle: {
                //         color: '#dddc6b'
                //     }
                // },
                // formatter: "{a} <br/>{b}: {c}",
                // textStyle: { // style of legend text
                //             Color:'#fff', //text color
                //             fontSize: 12 // text size
                // }
            },
            grid: {
                left: '2%',
                top:'20px',
                right: '2%',
                bottom: '15%',
               containLabel: true
            },
            // dataZoom: [{
            //     type: 'inside'
            // }, {
            //     type: 'slider',
            // }],
            xAxis: {
                type: 'category',
                data: Object.keys(vue.city_sentiment[keys[0]]),
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
                        interval: 0,
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
            legend:{
                show: true,
                textStyle:{
                    color: "#fff"
                }
            },
            series: [sentdis_data[0], sentdis_data[1], sentdis_data[2], sentdis_data[3], sentdis_data[4]]
        };
        
        var wordCloud_option = {
            toolbox: {
                feature: {
                    // dataZoom: {
                    //     yAxisIndex: false
                    // },
                    saveAsImage: {
                        pixelRatio: 2
                    }
                }
            },
            tooltip: {
                show: true
            },
            series: [tophashtags_data[0]]
        };        
        
        //--------------------------- Charts Initialisation ---------------------------\\

        console.log(langdis_data[0])
        // 语言分布图初始化数据
        langChart.setOption(lang_option);
        timeChart.setOption(time_option);
        sentChart.setOption(sent_option);
        //使用制定的配置项和数据显示图表
        wordCloud.setOption(wordCloud_option);
        window.addEventListener("resize",function(){
            langChart.resize();
            timeChart.resize();
            sentChart.resize();
            wordCloud.resize();
        });


        optionXyMap01 = {
            timeline: {
                data: year,
                axisType: 'category',
                autoPlay: true,
                playInterval: 3000,
                left: '10%',
                right: '10%',
                bottom: '3%',
                width: '80%',
                label: {
                    normal: {
                        textStyle: {
                            color: '#ddd'
                        }
                    },
                    emphasis: {
                        textStyle: {
                            color: '#fff'
                        }
                    }
                },
                symbolSize: 10,
                lineStyle: {
                    color: '#555'
                },
                checkpointStyle: {
                    borderColor: '#777',
                    borderWidth: 2
                },
                controlStyle: {
                    showNextBtn: true,
                    showPrevBtn: true,
                    normal: {
                        color: '#666',
                        borderColor: '#666'
                    },
                    emphasis: {
                        color: '#aaa',
                        borderColor: '#aaa'
                    }
                },

            },
            baseOption: {
                animation: true,
                animationDuration: 1000,
                animationEasing: 'cubicInOut',
                animationDurationUpdate: 1000,
                animationEasingUpdate: 'cubicInOut',
                grid: {
                    right: '3%',
                    top: '15%',
                    bottom: '65%',
                    width: '20%'
                },
                tooltip: {
                    trigger: 'axis', // hover触发器 时间轴
                    axisPointer: { // 坐标轴指示器，坐标轴触发有效
                        type: 'shadow', // 默认为直线，可选为：'line' | 'shadow'
                        shadowStyle: {
                            color: 'rgba(150,150,150,0.1)' //hover颜色
                        }
                    }
                },
                toolbox: {
                    feature: {
                        // dataZoom: {
                        //     yAxisIndex: false
                        // },
                        saveAsImage: {
                            pixelRatio: 2
                        }
                    }
                },
                geo: { //地图设置
                    // nameProperty: "STATE_NAME",
                    show: true,
                    map: 'australia',
                    roam: false,
                    zoom: 1,
                    layoutCenter: ['50%', '50%'],
                    // If width-height ratio is larger than 1, then width is set to be 100.
                    // Otherwise, height is set to be 100.
                    // This makes sure that it will not exceed the area of 100x100
                    layoutSize: 500,
                    // center: [133.7751, -25.2744],
                    tooltip: {
                        trigger: 'item',
                        formatter: (p) => {
                            let val = p.value[2];
                            if (window.isNaN(val)) {
                                val = 0;
                            }
                            let txtCon =
                                "<div style='text-align:left'>" + p.name + ":<br />Total Tweets：" + val.toFixed(2) + '</div>';
                            return txtCon;
                        }
                    },
                    label: {
                        emphasis: {
                            show: false
                        }
                    },
                    itemStyle: {
                        normal: {
                            // areaColor: '#4c60ff',
                            // borderColor: '#002097',
                            borderColor: 'rgba(147, 235, 248, 1)',
                            borderWidth: 1,
                            areaColor: {
                                type: 'radial',
                                x: 0.5,
                                y: 0.5,
                                r: 0.8,
                                colorStops: [{
                                    offset: 0,
                                    color: 'rgba(147, 235, 248, 0)' // 0% 处的颜色
                                }, {
                                    offset: 1,
                                    color: 'rgba(147, 235, 248, .2)' // 100% 处的颜色
                                }],
                                globalCoord: false // 缺省为 false
                            },
                            shadowColor: 'rgba(128, 217, 248, 1)',
                            // shadowColor: 'rgba(255, 255, 255, 1)',
                            shadowOffsetX: -2,
                            shadowOffsetY: 2,
                            shadowBlur: 10
                        },
                        emphasis: {
                            // areaColor: '#293fff',
                            areaColor: '#389BB7',
                            borderWidth: 0
                        }
                    }
                },
            },
            options: []

        };
    // geo: {
    //     map: 'china',
    //     label: {
    //         emphasis: {
    //             show: false
    //         }
    //     },
    //     roam: false,//禁止其放大缩小
    //     itemStyle: {
    //         normal: {
    //             areaColor: '#4c60ff',
    //             borderColor: '#002097'
    //         },
    //         emphasis: {
    //             areaColor: '#293fff'
    //         }
    //     }
    // },
        for (var n = 0; n < year.length; n++) {
            optionXyMap01.options.push({
                // backgroundColor: '#013954',
                title:
                    [
                    // {
                    //         text: 'Area Tweets',
                    //         left: '42%',
                    //         top: '8%',
                    //         textStyle: {
                    //             color: '#fff',
                    //             fontSize: 25
                    //         }
                    //     },
                        {
                            id: 'statistic',
                            text: year[n] + "Tweets",
                            left: '70%',
                            top: '8%',
                            textStyle: {
                                color: '#fff',
                                fontSize: 25
                            }
                        }
                    ],
                xAxis: {
                    type: 'value',
                    scale: true,
                    position: 'top',
                    min: 0,
                    boundaryGap: false,
                    splitLine: {
                        show: false
                    },
                    axisLine: {
                        show: false
                    },
                    axisTick: {
                        show: false
                    },
                    axisLabel: {
                        show: false,
                        margin: 5,
                        textStyle: {
                            color: '#aaa'
                        }
                    },
                },
                yAxis: {
                    type: 'category',
                    //  name: 'TOP 20',
                    nameGap: 16,
                    axisLine: {
                        show: true,
                        lineStyle: {
                            color: '#ddd'
                        }
                    },
                    axisTick: {
                        show: false,
                        lineStyle: {
                            color: '#ddd'
                        }
                    },
                    axisLabel: {
                        interval: '0',
                        textStyle: {
                            color: '#ddd'
                        }
                    },
                    data: categoryData[n]
                },
                tooltip:{
                    show: true
                },
                series: [
                    //地图
                    {
                        type: 'map',
                        map: 'australia',
                        geoIndex: 0,
                        aspectScale: 0.75, //长宽比
                        showLegendSymbol: false, // 存在legend时显示
                        // nameProperty: 'STATE_NAME',
                        label: {
                            normal: {
                                show: false
                            },
                            emphasis: {
                                show: false,
                                textStyle: {
                                    color: '#fff'
                                }
                            }
                        },
                        roam: true,
                        itemStyle: {
                            normal: {
                                areaColor: '#031525',
                                borderColor: '#FFFFFF',
                            },
                            emphasis: {
                                areaColor: '#2B91B7'
                            }
                        },
                        animation: false,
                        data: mapData
                    },
                    //地图中闪烁的点
                    {
                        //  name: 'Top 5',
                        type: 'effectScatter',
                        coordinateSystem: 'geo',
                        data: convertData(mapData[n].sort(function(a, b) {
                            return b.value - a.value;
                        }).slice(0, 20)),
                        symbolSize: function(val) {
                            return val[2] / 10000;
                        },
                        showEffectOn: 'render',
                        rippleEffect: {
                            brushType: 'stroke'
                        },
                        hoverAnimation: true,
                        label: {
                            normal: {
                                color: 'rgba(255, 255, 255, 0.9)',
                                formatter: '{b}',
                                position: 'right',
                                show: true
                            }
                        },
                        itemStyle: {
                            normal: {
                                color: colors[colorIndex][n],
                                shadowBlur: 10,
                                shadowColor: colors[colorIndex][n]
                            }
                        },
                        zlevel: 1
                    },
                    //柱状图
                    {
                        zlevel: 1.5,
                        type: 'bar',
                        symbol: 'none',
                        itemStyle: {
                            normal: {
                                color: colors[colorIndex][n]
                            }
                        },
                        data: barData[n]
                    }
                ]
            })
        }
        myChart.setOption(optionXyMap01);
        window.addEventListener("resize",function(){
            myChart.resize();
        });


        myChart.on('click', function (params) {
            var city = params.name;
            console.log(city)
            var index = keys.findIndex(function(item) {
                console.log(item)
                return item == city.toLowerCase();
            });
            // option['title']['text'] = city;
            lang_option['title']['text'] = langdis_data[index].name;
            // lang_option['xAxis']['data'] = Object.keys(vue.city_lang[keys[index]]);
            lang_option['visualMap']['min'] = Math.min(...Object.values(vue.city_lang[keys[index]]));
            lang_option['visualMap']['max'] = Math.max(...Object.values(vue.city_lang[keys[index]]));
            lang_option['series'] = [langdis_data[index]];
            langChart.setOption(lang_option);

            time_option['title']['text'] = timedis_data[index].name;
            time_option['xAxis']['data'] = Object.keys(vue.city_time_dis[keys[index]]);
            time_option['series'] = [timedis_data[index]];
            timeChart.setOption(time_option);

            // sent_option['title']['text'] = sentdis_data[index].name.toUpperCase();
            // sent_option['xAxis']['data'] = Object.keys(vue.city_sentiments[keys[index]]);
            // sent_option['series'] = [sentdis_data[index]];
            // sentChart.setOption(sent_option);

            // wordCloud_option['title']['text'] = tophashtags_data[index].name.toUpperCase();
            // wordCloud_option['xAxis']['data'] = Object.keys(vue.city_hashtags[keys[index]]);
            wordCloud_option['series'] = [tophashtags_data[index]];
            console.log(tophashtags_data[index])
            wordCloud.setOption(wordCloud_option);
        });

        window.addEventListener("resize",function(){
            langChart.resize();
        });

    }

})
},13000)
