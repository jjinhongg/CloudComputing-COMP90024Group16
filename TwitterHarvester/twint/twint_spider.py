# Group 16

# Team members:

# Zenan Ji (Student ID: 1122396) - city: Nanjing

# Weijie Ye (Student ID: 1160818) - city: Fuzhou

# Wenqin Liu (Student ID: 807291) - city: Guangdong

# Jinhong Yong (Student ID: 1198833) - city: Kuala Lumpur

# Zixuan Zeng (Student ID: 1088297) - city: Melbourne

import twint
import threading


def tweetCrawling(location, coordinate, range):
    outputf = '.'.join([location, "json"])
    print(outputf)
    c = twintCongig(coordinate, range, outputf)
    twint.run.Search(c)

def twintCongig(coordinate, range, outputf):
    geo = ",".join([str(coordinate[0]), str(coordinate[1]), range])
    c = twint.Config()
    c.Geo = geo
    c.Since = "2018-01-01"
    c.Until = "2019-07-28"
    # c.Limit = 1000
    c.Output = outputf
    c.Store_json = True
    return c

def run_spider():
    cities = ["Brisbane"]
    cities_geo = {"Melbourne": (-37.8136, 144.9631), "Sydney": (-33.8688, 151.2093),
                  "Adelaide": (-34.9285, 138.6007), "Canberra": (-35.2809, 149.1300),
                  "Brisbane": (-27.4705, 153.0260)}

    for city in cities:
        tweetCrawling(city, cities_geo[city], "20km")
