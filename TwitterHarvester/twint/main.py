# Group 16

# Team members:

# Zenan Ji (Student ID: 1122396) - city: Nanjing

# Weijie Ye (Student ID: 1160818) - city: Fuzhou

# Wenqin Liu (Student ID: 807291) - city: Guangdong

# Jinhong Yong (Student ID: 1198833) - city: Kuala Lumpur

# Zixuan Zeng (Student ID: 1088297) - city: Melbourne

import threading
from twint_spider import run_spider
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
        # schedule.run_pending()


