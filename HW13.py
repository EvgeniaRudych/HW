# 1. Write the method that return the number of threads currently in execution.
# Also prepare the method that will be executed with threads and run during the first method counting.
from threading import Thread
import time
import threading
import datetime


def foo1():
    for x in range(5):
        print(f"from first thread: {x}")
    time.sleep(1)


def foo2():
    for x in range(5):
        print(f"from second thread: {x}")
    time.sleep(1)


def thread_counting():
    print(f" The active count is {threading.activeCount()}")


thread_1 = Thread(target=foo1)
thread_2 = Thread(target=foo2)

start = time.time()

thread_1.start()
thread_2.start()
while threading.activeCount() > 1:
    thread_counting()
    time.sleep(1)
thread_1.join()
thread_2.join()

# 2. Print current date by using 2 threads.
# #1. Define a subclass using Thread class.
# #2. Instantiate the subclass and trigger the thread.

class CurrentDate(Thread):

    def run(self) -> None:
        print(f"The current date is {datetime.date.today()}")
        time.sleep(1)

thread_3 = CurrentDate()
thread_4 = CurrentDate()
thread_3.start()
thread_4.start()
thread_3.join()
thread_4.join()


# 3. Use Pool.apply() to get the row wise common items in list_a and list_b.
list_a = [[1, 2, 3], [5, 6, 7, 8], [10, 11, 12], [20, 21]]
list_b = [[2, 3, 4, 5], [6, 9, 10], [11, 12, 13, 14], [21, 24, 25]]
import time
from timeit import default_timer as timer
from multiprocessing import Pool
# 3. Use Pool.apply() to get the row wise common items in list_a and list_b.
list_a = [[1, 2, 3], [5, 6, 7, 8], [10, 11, 12], [20, 21]]
list_b = [[2, 3, 4, 5], [6, 9, 10], [11, 12, 13, 14], [21, 24, 25]]
import time
from timeit import default_timer as timer
from multiprocessing import Pool


def common_items(x, y):
    return list(map(lambda a, b: set(a).intersection(b), x, y))

with Pool() as pool:
    print(pool.apply(common_items, args=(list_b, list_a)))

# 4. Divide the work between 2 methods: print_cube that returns the cube of number
# and print_square that returns the square of number. These two methods should be executed by using 2 different processes.
from multiprocessing import Pool, Process
from concurrent.futures import ProcessPoolExecutor


def print_cube(num):
    print(f'Cube of {num} is {num ** 3} ')
    return num ** 3


def print_square(num):
    print(f'Square of {num} is {num ** 3} ')
    return num ** 2


with ProcessPoolExecutor(max_workers=2) as pool:
    pool.submit(print_cube)
    pool.submit(print_square)

process1 = Process(name="Process1", target=print_cube, args=(3,))
process2 = Process(name="Process2", target=print_square, args=(9,))
process1.start()
process2.start()






