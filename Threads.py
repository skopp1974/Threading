# Python program to illustrate the concept
# of threading
import threading
import os
import time

# global variable
g_id = 100
lock = threading.Lock()
sleep_duration = 1


# Enable synchronous execution by setting enable_lock to 1
enable_sync = 1


def up():
    global g_id
    # auto_lock = ClsLock()
    g_id += 1


def down():
    global g_id
    # auto_lock = ClsLock()
    g_id -= 1


# ------------------------------
class ClsLock:

    # Initializing
    def __init__(self):
        if bool(enable_sync):
            print('Lock Acquired.')
            lock.acquire()

    # Deleting (Calling destructor)
    def __del__(self):
        if bool(enable_sync):
            print('Lock released.')
            lock.release()
# ------------------------------


def task1():
    print("Task 1 assigned to thread: {}".format(threading.current_thread().name))
    print("ID of process running task 1: {}".format(threading.current_thread().ident))
    global g_id, sleep_duration
    synclock = ClsLock()
    print("Task 1 - BEFORE Updated ID: ", g_id)
    up()
    time.sleep(sleep_duration)
    down()
    print("Task 1 - AFTER Updated ID: ", g_id)
    del synclock  # Explicitly release lock


def task2():
    print("Task 2 assigned to thread: {}".format(threading.current_thread().name))
    print("ID of process running task 2: {}".format(threading.current_thread().ident))
    global g_id, sleep_duration
    synclock = ClsLock()  # This will auto release lock when goes out of scope
    print("Task 2 - BEFORE Updated ID: ", g_id)
    up()
    time.sleep(sleep_duration)
    down()
    print("Task 2 - AFTER Updated ID: ", g_id)


def task3():
    print("Task 3 assigned to thread: {}".format(threading.current_thread().name))
    print("ID of process running task 2: {}".format(threading.current_thread().ident))
    global g_id, sleep_duration
    synclock = ClsLock()  # This will auto release lock when goes out of scope
    print("Task 3 - BEFORE Updated ID: ", g_id)
    up()
    time.sleep(sleep_duration)
    down()
    print("Task 3 - AFTER Updated ID: ", g_id)


def task4():
    print("Task 4 assigned to thread: {}".format(threading.current_thread().name))
    print("ID of process running task 4: {}".format(threading.current_thread().ident))
    global g_id, sleep_duration
    synclock = ClsLock()  # This will auto release lock when goes out of scope
    print("Task 4 - BEFORE Updated ID: ", g_id)
    up()
    time.sleep(sleep_duration)
    down()
    print("Task 4 - AFTER Updated ID: ", g_id)


def task5():
    print("Task 5 assigned to thread: {}".format(threading.current_thread().name))
    print("ID of process running task 5: {}".format(threading.current_thread().ident))
    global g_id, sleep_duration
    synclock = ClsLock()  # This will auto release lock when goes out of scope
    print("Task 5 - BEFORE Updated ID: ", g_id)
    up()
    time.sleep(sleep_duration)
    down()
    print("Task 5 - AFTER Updated ID: ", g_id)


if __name__ == "__main__":
    start = time.time()
    # print ID of current process
    print("ID of process running main program: {}".format(os.getpid()))

    # print name of main thread
    print("Main thread name: {}".format(threading.main_thread().name))

    t1 = threading.Thread(target=task1, name='t5')
    t2 = threading.Thread(target=task2, name='t2')
    t3 = threading.Thread(target=task3, name='t3')
    t4 = threading.Thread(target=task4, name='t4')
    t5 = threading.Thread(target=task5, name='t5')

    # starting threads
    t1.start()
    t2.start()
    t3.start()
    t4.start()
    t5.start()

    # wait until all threads finish
    t1.join()
    t2.join()
    t5.join()
    t4.join()
    t5.join()
    end = time.time()
    print('Elapsed time: [{0}] Sec\n'.format(end-start))

