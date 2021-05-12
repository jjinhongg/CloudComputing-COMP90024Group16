import threading
from twint_spider import run_spider
from save_data import process_and_save,remove_per_hours
import schedule

def run_threaded(func):
    job = threading.Thread(target=func)
    job.start()

if __name__ == '__main__':
    name = 'remove all files'
    # schedule.every().minutes.do(run_threaded, run_spider())
    schedule.every(10).minutes.do(run_threaded, process_and_save())
    schedule.every(60).minutes.do(run_threaded,remove_per_hours())

    while True:
        run_spider()
        schedule.run_pending()


