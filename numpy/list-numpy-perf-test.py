
import numpy as np
import time
N= 1_000_000

#calculation using python list
list1 = list(range(N))
list2 = list(range(N))

start = time.time()
result_list = [ list1[i] * list2[i] for i in  range(N)]
end = time.time()
print("Python List Time : ", round(end-start,5), "seconds")

#calculation using numpy arrays
array1 = np.array(range(N))
array2 = np.array(range(N))
start = time.time()
result_nparray =  array1* array2 # Vectorized Operation
end = time.time()
print("Python array Time : ", round(end-start,5), "seconds")

