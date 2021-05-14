import threading
from tweepy_spider import run_spider
from save_data import process_and_save,couchdb_init
import schedule
import nltk


if __name__ == '__main__':
    nltk.download('punkt')
    # name = 'remove all files'
    # schedule.every().minutes.do(run_threaded, run_spider())
    # schedule.every(1).minutes.do(run_threaded, process_and_save())
    # schedule.every(60).minutes.do(run_threaded,remove_per_hours())
    # schedule.every(10).minutes.do(run_spider, name)
    # schedule.every(1).minutes.do(process_and_save)
    # schedule.every(60).minutes.do(remove_per_hours, name)
    # client = couchdb_init()
    while True:
        # client = couchdb_init()
        run_spider()
        client = couchdb_init()
        process_and_save(client)