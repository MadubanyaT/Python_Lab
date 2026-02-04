import threading
import time
from tabnanny import verbose

t = 2
def Thread_message(threadname, name1, name2, slept):
    time.sleep(slept)
    print(f"Thread name: {threadname}, Name 1: {name1}, Name 2: {name2}")


thread1 = threading.Thread(target=Thread_message, args=("T1", "A", "B", 5))
thread2 = threading.Thread(target=Thread_message, args=("T2", "C", "D", 2))

thread1.start()
thread2.start()

thread1.join()
thread2.join()



