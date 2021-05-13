import threading
from tweepy_spider import run_spider
from save_data import process_and_save,remove_per_hours
import schedule


if __name__ == '__main__':
    # name = 'remove all files'
    # schedule.every().minutes.do(run_threaded, run_spider())
    # schedule.every(1).minutes.do(run_threaded, process_and_save())
    # schedule.every(60).minutes.do(run_threaded,remove_per_hours())
    # schedule.every(10).minutes.do(run_spider, name)
    # schedule.every(1).minutes.do(process_and_save)
    # schedule.every(60).minutes.do(remove_per_hours, name)
    while True:
        run_spider()
        process_and_save()