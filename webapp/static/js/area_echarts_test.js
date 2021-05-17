var colors = [
    ["#1DE9B6", "#F46E36", "#04B9FF", "#5DBD32", "#FFC809", "#FB95D5", "#BDA29A", "#6E7074", "#546570", "#C4CCD3"],
    ["#37A2DA", "#67E0E3", "#32C5E9", "#9FE6B8", "#FFDB5C", "#FF9F7F", "#FB7293", "#E062AE", "#E690D1", "#E7BCF3", "#9D96F5", "#8378EA", "#8378EA"],
    ["#DD6B66", "#759AA0", "#E69D87", "#8DC1A9", "#EA7E53", "#EEDD78", "#73A373", "#73B9BC", "#7289AB", "#91CA8C", "#F49F42"],
];
var colorIndex = 0;

$(function () {
    map();
    function map() {
        var pieChart = echarts.init(document.getElementById('echart2')); //初始化饼图
        // 基于准备好的dom，初始化echarts实例
        var myChart = echarts.init(document.getElementById('map_1'));
        var mapData = [
            [],
            [],
            []
        ];
    
        /*柱子Y名称*/
        var categoryData = [];
        var barData = [];
        var pie_data = [];
    
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

        var myChart = echarts.init(document.getElementById('map_1'));
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

        var piecolor=['#00ffff','#00cfff','#006ced','#ffe000','#ffa800']
        // var piecolor=['#00ffff','#00cfff','#006ced','#ffe000','#ffa800','#ff5b00','#ff3000']
        for (var i = 0; i < keys.length; i++) {
            var keyname = keys[i]; 
            pie_data.push({
                // zlevel: 2,
                // z:3,
                name: keyname, //city
                type: 'pie',
                radius: ['50%', '70%'],
                center: ['50%', '50%'],
                color: ['#065aab', '#066eab', '#0682ab', '#0696ab', '#06a0ab','#06b4ab','#06c8ab','#06dcab','#06f0ab'],
                data: [
                    {value: lang1, name: 'EN'},
                    {value: lang2, name: 'CN'},
                    {value: lang3, name: 'JP'},
                    {value: lang4, name: 'KR'},
                    {value: lang5, name: 'FR'}
                ].sort(function (a, b) { return a.value - b.value; }),
                roseType: 'radius',
                label: {
                    color: 'rgba(255, 255, 255, 0.3)',
                    normal: {
                        Show: true, // ​​whether to display the label
                        //// The location of the tag. The 'outside' is outside the pie slice and is connected to the corresponding sector by a visual guide. 'inside', 'inner' Same as 'inside', inside the pie slice. 'center' is at the center of the pie chart.
                        position: 'left',
                        // The content of the displayed label
                        //a (series name), b (data item name), c (number), d (percentage)
                        formatter: "{b}:{c}({d}%)", 
                        emphasis: {
                                 //The label style displayed by the mouse on the ring
                            show: true,
                            textStyle: {
                                fontSize: '10',
                                fontWeight: 'bold'
                            }
                        }
                    }
                },
                labelLine: {
                    lineStyle: {
                        // color: 'rgba(255, 255, 255, 0.3)'
                    },
                    smooth: 0.2,
                    length: 10,
                    length2: 20
                },
                itemStyle: {
                    // color: '#c23531',
                    shadowBlur: 200,
                    shadowColor: 'rgba(0, 0, 0, 0.5)',
                    label:{  
                        show:true,  
                        formatter:'{d}%'  
                    }, 
                },
    
                animationType: 'scale',
                animationEasing: 'elasticOut',
                animationDelay: function (idx) {
                    return Math.random() * 200;
                }
            })
        }



        // 饼状图配置
        var option = {
            // backgroundColor: '#2c343c',
            title: {
                zlevel: 2,
                // z:3,
                text: pie_data[0]['name'],
                top: 'middle',
                left: 'center',
                textStyle: {
                    color: '#fff',
                    fontSize: '14'
                }
            },
            legend: {
                // The mode selected by the legend controls whether the display state of the series can be changed by clicking on the legend. The legend selection is turned on by default and can be set to false to close.
                selectedMode: true, 
                /* orient: 'vertical', */
                /* x : 'right', //the legend is shown on the right
                y: 'center', */ //The legend is centered above the vertical display
                bottom:0,
                itemWidth: 10, // the width of the legend mark
                itemHeight: 10, //Graph height of the legend mark
                Data:['EN', 'CN', 'JP', 'KR', 'FR'],
                textStyle: { // style of legend text
                color: 'rgba(255,255,255,.5)',
                // Color: '#A6A8B6', //text color
                fontSize: 10 // text size
                }
            },   		  
            tooltip: {
                trigger: 'item',
                formatter: "{a} <br/>{b}: {c} ({d}%)",
                textStyle: { // style of legend text
                            Color:'#fff', //text color
                            fontSize: 10 // text size
                }
            },
            visualMap: {
                show: false,
                min: 0,
                max: 300,
                inRange: {
                    colorLightness: [0.5, 1]
                }
            },
            series: [pie_data[0]]
        };
        // 饼状图初始化数据
        pieChart.setOption(option);
        window.addEventListener("resize",function(){
            pieChart.resize();
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
                geo: { //地图设置
                    nameProperty: "STATE_NAME",
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
                    [{
                            text: 'Area Tweets',
                            left: '42%',
                            top: '8%',
                            textStyle: {
                                color: '#fff',
                                fontSize: 25
                            }
                        },
                        {
                            id: 'statistic',
                            text: year[n] + " Statistics",
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
                        margin: 2,
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
                        interval: 0,
                        textStyle: {
                            color: '#ddd'
                        }
                    },
                    data: categoryData[n]
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
                            return val[2] / 10;
                        },
                        showEffectOn: 'render',
                        rippleEffect: {
                            brushType: 'stroke'
                        },
                        hoverAnimation: true,
                        label: {
                            normal: {
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
                return item == city;
            });
            // option['title']['text'] = city;
            option['title']['text'] = pie_data[index].name;
            option['series'] = [pie_data[index]];
            pieChart.setOption(option);
        });

        window.addEventListener("resize",function(){
            pieChart.resize();
        });

    }

})

