// # Group 16
//
// # Team members:
//
//     # Zenan Ji (Student ID: 1122396) - city: Nanjing
//
// # Weijie Ye (Student ID: 1160818) - city: Fuzhou
//
// # Wenqin Liu (Student ID: 807291) - city: Guangdong
//
// # Jinhong Yong (Student ID: 1198833) - city: Kuala Lumpur
//
// # Zixuan Zeng (Student ID: 1088297) - city: Melbourne

var ec_result = echarts.init(document.getElementById('analysisResult'))
var ec_result_option = {
    title: {
        text: '某站点用户访问来源',
        subtext: '纯属虚构',
        left: 'center'
    },
    tooltip: {
        trigger: 'item'
    },
    legend: {
        orient: 'vertical',
        left: 'left',
    },
    series: [
        {
            name: '访问来源',
            type: 'pie',
            radius: '50%',
            data: [
                {value: 1048, name: '搜索引擎'},
                {value: 735, name: '直接访问'},
                {value: 580, name: '邮件营销'},
                {value: 484, name: '联盟广告'},
                {value: 300, name: '视频广告'}
            ],
            emphasis: {
                itemStyle: {
                    shadowBlur: 10,
                    shadowOffsetX: 0,
                    shadowColor: 'rgba(0, 0, 0, 0.5)'
                }
            }
        }
    ]
};

ec_result.setOption(ec_result_option)