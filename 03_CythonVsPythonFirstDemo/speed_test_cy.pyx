import numpy as np
import numpy.random as random

def compute_cy():
    # let's create a very large matrix
    # and a large vector
    N = 1000
    S = 1

    # initialize them to something random
    A = random.rand(N,N)
    b = random.rand(N)
    c = [0]*N

    # we do a matrix-vector dot product for a few times
    for k in range(S):
        for i in range(N):
            for j in range(N):
                c[i] += A[i,j]*b[j]

    print("Cython done.")




