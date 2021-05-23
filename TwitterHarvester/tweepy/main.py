
from tweepy_spider import run_spider
from save_data import process_and_save,couchdb_init
from update_hashtags import update_hashtags
import time
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
    start_time = time.time()
    while True:
        # client = couchdb_init()
        try:
            run_spider()
        except:
            continue
        client = couchdb_init()
        process_and_save(client)

        current_time = time.time()
        if current_time - start_time >= 600:
            try:
                update_hashtags()
                start_time = time.time()
            except:
                pass
