# Decorator Intent - why, how

'''
Say u have target() n prod used by muliple teams multiple place, you client wants to measure time taken
on every invocation,
 -> u cannot change target() in prod
 ->
decorators helps us using closures concept
creating inner func  - executor fn - returning its address to called func

target = profiler(target)

simply putting - u write decorate inner func to decoarate target() and returning address of decorator(executor() hear)
just changing the address of target whenvet target is called
'''

from time import sleep, time

def profiler(x):
    def executor():
        start_time = time()
        x()
        end_time = time()
        print("Total Time Taken {}".format(end_time - start_time))
    return executor

@profiler
def target():
    print("Calculating")
    sleep(3)
    print("Calcuation Done")

target()

'''
this is done by interpretor when @profiler is used- wherever target(100  address) is called--> executes profiler which returns
executor() func address (102)-which when called applies our logic and also calls actual target() -100 address

target = profiler(target)
target()

'''
'''
How it executes
from time import sleep, time

# tested & Production, shouldn't modified
# profiler -> 100 address
def profiler(x):      # x => 101
    # executor => 102
    def executor():
        start_time = time()
        x()
        end_time = time()
        print("Total Time Taken {}".format(end_time - start_time))
    return executor
# Target => 101  (RefCount: 1)
@profiler
def target():
    print("Calculating")
    sleep(3)
    print("Calcuation Done")
# target => 102
######target = profiler(target)
# Module 1
target()
'''