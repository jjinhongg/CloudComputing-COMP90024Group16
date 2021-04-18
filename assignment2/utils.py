
import random

def count_all_tweet():
    return random.randint(1,9999)

def get_tweeters():
    test = {'1':'','2':'','3':'','4':'','5':''}
    for i in range(5):
        res = 'I am ' + str(random.randint(1,99)) + ' years'
        test[str(i)] = res
    return test


