import numpy as np
array_1 = np.random.uniform(0, 1000, size=(3000, 2000)).astype(np.intc)
array_2 = np.random.uniform(0, 1000, size=(3000, 2000)).astype(np.intc)
a, b, c = 4, 3, 9

import time
import compute_py
import compute_cy

def compute_np(array_1, array_2, a, b, c):
    return np.clip(array_1, 2, 10) * a + array_2 * b + c

t1 = time.time()
compute_py.compute(array_1, array_2, a, b, c)
t2 = time.time()

t3 = time.time()
compute_cy.compute(array_1, array_2, a, b, c)
t4 = time.time()

t5 = time.time()
compute_np(array_1, array_2, a, b, c)
t6 = time.time()

print("Python: {}, Cython: {}, Numpy: {}".format(t2-t1,t4-t3, t6-t5))
