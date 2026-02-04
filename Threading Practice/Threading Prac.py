# Think of it as highway, if we have one lane then cars will have to follow each other (traffic) but if we have more than one
#       then cars will use other lanes and there won't be any traffic.

import threading
import time
import random

def print_names():
    for name in ('Ben', 'Jack', 'Thabo', 'Lebo', 'Kat'):
        print(name)
        time.sleep(random.uniform(0.5, 1.5)) # sleeps for this period

def print_age():
    for num in range(5):
        print(random.randint(20, 40))
        time.sleep(random.uniform(0.5, 1.5)) # Just illustration of when a thread is taking too long e.g downloading a file

# WITH THREADING
thread1 = threading.Thread(target=print_names) # Parameters of a function are passed via args argument as a tuple e.g args=(1, 2)
thread2 = threading.Thread(target=print_age)

# starting the thread
thread1.start()
thread2.start()

# Think of join as joining the main thread (It's going to wait for both threads (thread1, thread2) to complete before the program
# stops)
thread1.join()
thread2.join()


# NO THREADING
# print_names()
# print_age()
