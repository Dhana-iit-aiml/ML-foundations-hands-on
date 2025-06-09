
# when u decorate the arguments should match exactly everywhere
'''
however we cannot keep changind prototype-arg of func to match also u shouldn't change exsiting functionality
hence use *args,**kwargs to match any arguments

'''

from time import sleep, time
def profiler(x):
    def executor(*args,**kwargs):
        start_time = time()
        ret = x(*args,**kwargs)
        end_time = time()
        print("Total Time Taken {}".format(end_time - start_time))
        return ret
    return executor
@profiler
def task1(a):
    sleep(2)
    print (f"Value of a is {a}")
@profiler
def task2(a,b):
    sleep(2)
    print (f"Value2 of a&b is {a} {b}")
    return a*b
# task1(99)
result =task2(99,100)
print (result)

