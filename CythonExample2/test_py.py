import speed_test_py
import speed_test_cy
import time

t1 = time.time()
speed_test_py.compute_py()
t2 = time.time()

t3 = time.time()
speed_test_cy.compute_cy()
t4 = time.time()

print("Total time was ",t2-t1)
print("Total time was ",t4-t3)


