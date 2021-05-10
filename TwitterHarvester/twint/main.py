import threading
import time
from save_data import *

if __name__ == '__main__':
    threads = []
    threads.append(threading.Thread(target=run_spider()))
    # run_spider()
    threads.append(threading.Thread(target=process_and_save()))
    # process_and_save()
    for t in threads:
        t.start()
