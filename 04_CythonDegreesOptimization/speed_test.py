import numpy as np
array_1 = np.random.uniform(0, 500, size=(1500, 1000)).astype(np.intc)
array_2 = np.random.uniform(0, 500, size=(1500, 1000)).astype(np.intc)
a, b, c = 4, 3, 9

import time
import compute_py
import compute_cy1
import compute_cy2
import compute_cy3

def compute_np(array_1, array_2, a, b, c):
    return np.clip(array_1, 2, 10) * a + array_2 * b + c

t1 = time.time()
compute_py.compute(array_1, array_2, a, b, c)
t2 = time.time()

t3 = time.time()
compute_cy1.compute(array_1, array_2, a, b, c)
t4 = time.time()

t5 = time.time()
compute_cy2.compute(array_1, array_2, a, b, c)
t6 = time.time()

t7 = time.time()
compute_cy3.compute(array_1, array_2, a, b, c)
t8 = time.time()

t9 = time.time()
compute_np(array_1, array_2, a, b, c)
t10 = time.time()

print("Python: {}, Numpy: {}".format(t2-t1,t10-t9))
print("Cython1: {} Cython2: {} Cython3: {}".format(t4-t3,t6-t5,t8-t7))
