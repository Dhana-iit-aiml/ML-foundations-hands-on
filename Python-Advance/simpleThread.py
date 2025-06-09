
from  threading import  Thread
import time
def task1():
    while True:
        print("happy wednesday...")
        time.sleep(2)

def task2():
    while True:
        print("happy october...")
        time.sleep(3)

t1 = Thread(target=task1)
t1.start()
t2 = Thread(target=task2)
t2.start()