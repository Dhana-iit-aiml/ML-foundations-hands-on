from time import sleep, time
from datetime import datetime
def profiler(x):
    def executor(*args,**kwargs):
        start_time = time()
        ret = x(*args,**kwargs)
        end_time = time()
        print("Total Time Taken {}".format(end_time - start_time))
        return ret
    return executor
def restrict_time(x):
    def executor(*args,**kwargs):
        hour= datetime.now().hour
        if 20<hour<23:
            print ("Restricted Timing")
        else:
            return x(*args, **kwargs)
    return executor
def logger(x):
    def executor(*args,**kwargs):
        with open("log.log","a") as file:
            file.write("Executed {}\n at {}".format(x.__name__,datetime.now()))
        return x(*args, **kwargs)
    return executor


@restrict_time
@profiler
@logger
def task1(a):
    sleep(2)
    print (f"Value of a is {a}")
@restrict_time
@profiler
@logger
def task2(a,b):
    sleep(2)
    print (f"Value2 of a&b is {a} {b}")
    return a*b
result= task1(99)
print (result)