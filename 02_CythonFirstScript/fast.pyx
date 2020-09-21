
def fib(n):
    """ Computes n-th element of the Fibonacci sequence """

    i = 0
    j = 1
    res = i + j
    for k in range(n-1):
        tmp = i
        i = j
        j += tmp

    return j

def mul(a, b):
    return a*b




