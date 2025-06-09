from time import time, sleep
'''
we have to simulate this, we need return decorator address
we can use __call__ method of a class which gets called for every time call class
target = profiler(target)
'''
class profiler:
    def __init__(self, function):
        self.function = function
    def __call__(self, *args, **kwargs):
        start_time = time()
        ret = self.function(*args, **kwargs)
        end_time = time()
        print("Total Time is {}".format(end_time - start_time))
        return ret


@profiler
def target():
    sleep(2)
    print("Target")

target()