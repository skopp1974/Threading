import datetime
import threading
from multiprocessing.dummy import Pool as ThreadPool
import os
import time

thred_count = 0
# Enable synchronous execution by setting enable_lock to 1

# ===============================================
enable_sleep = True
async_run = True
sleep_interval = 2 # Each thread worker will take approximately 6 secs due to 3  stages of sleep
max_workers = 100
max_parallel_threads = 100
# ===============================================

lock = threading.Lock()
g_id = 0


def up():
    global g_id
    g_id += 1


def down():
    global g_id
    g_id -= 1


# ------------------------------
class ClsLock:

    # Initializing
    def __init__(self):
        if not bool(async_run):
            #print('Lock Acquired.')
            lock.acquire()

    # Deleting (Calling destructor)
    def __del__(self):
        if not bool(async_run):
            #print('Lock released.')
            lock.release()
# ------------------------------


def update_shared_resource(n):
    global thred_count
    thred_count += 1
    print('New thread {0}\n'.format(thred_count))
    tid = threading.current_thread().ident
    # Before entering sync mode
    # if bool(enable_sleep):
    #     time.sleep(sleep_interval)
    #     print('Running Stage 1: {0}\n'.format(tid))
    #     time.sleep(sleep_interval)
    #     print('Running Stage 2: {0}\n'.format(tid))
    #     time.sleep(sleep_interval)
    #     print('Running Stage 3: {0}\n'.format(tid))

    # --------------------------------------------
    synclock = ClsLock()
    # Update shared resource g_id
    g_id = n

    # Corrupt shared resource g_id
    up()

    if bool(enable_sleep):
        print(
            '==> SLEEP: Thread ID: {0} - SHARED RESOUCE {1}\n'.format(tid, g_id))
        time.sleep(sleep_interval)
        print('    Running Stage 1: {0}\n'.format(tid))
        time.sleep(sleep_interval)
        print('    Running Stage 2: {0}\n'.format(tid))
        time.sleep(sleep_interval)
        print('    Running Stage 3: {0}\n'.format(tid))
    # Restore shared resource g_id
    down()
    print('<== AWAKE: Thread ID: {0} - SHARED RESOUCE {1}\n'.format(tid, g_id))
    return g_id  # + 10


# function to be mapped over
def run_parallel(__numbers, threads=2):
    pool = ThreadPool(threads)
    results = pool.map(update_shared_resource, __numbers)
    pool.close()
    pool.join()
    return results


if __name__ == "__main__":
    print('==> Time: {0}'.format(datetime.datetime.now()))
    start = time.time()
    # numbers = [1, 2, 3, 4, 5]
    #numbers  = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]
    numbers = []
    for k in range(0, max_workers):
        numbers.__iadd__([k])
    squaredNumbers = run_parallel(numbers, max_parallel_threads)

    # print(squaredNumbers)

    end = time.time()
    print('<== Time: {0}'.format(datetime.datetime.now()))
    print('Elapsed time: [{0}] Secs | Total async executions: {1}\n'.format(
        end-start, thred_count))
