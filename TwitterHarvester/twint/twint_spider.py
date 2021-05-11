import twint


def tweetCrawling(location, coordinate, range):
    outputf = '.'.join([location, "json"])
    print(outputf)
    c = twintCongig(coordinate, range, outputf)
    twint.run.Search(c)

def twintCongig(coordinate, range, outputf):
    geo = ",".join([str(coordinate[0]), str(coordinate[1]), range])
    c = twint.Config()
    c.Geo = geo
    # c.Since = "2019-01-01"
    # c.Until = date
    c.Limit = 100000
    c.Output = outputf
    c.Store_json = True
    return c

def run_spider():
    cities = ["Melbourne", "Sydney",
              "Adelaide", "Canberra",
              "Brisbane"]
    cities_geo = {"Melbourne": (-37.8136, 144.9631), "Sydney": (-33.8688, 151.2093),
                  "Adelaide": (-34.9285, 138.6007), "Canberra": (-35.2809, 149.1300),
                  "Brisbane": (-27.4705, 153.0260)}

    for city in cities:
        tweetCrawling(city, cities_geo[city], "20km")