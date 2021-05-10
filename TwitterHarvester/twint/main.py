import threading
from twint_spider import run_spider
from save_data import process_and_save
import schedule

def run_threaded(func):
    job = threading.Thread(target=func)
    job.start()

if __name__ == '__main__':

    schedule.every(10).minutes.do(run_threaded, run_spider())
    schedule.every(10).minutes.do(run_threaded, process_and_save())
    # threads = []
    # threads.append(threading.Thread(target=run_spider()))
    # # run_spider()
    # # threads.append(threading.Thread(target=process_and_save()))
    # # process_and_save()
    # for t in threads:
    #     t.start()

    while True:
        schedule.run_pending()


