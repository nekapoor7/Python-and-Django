""" the execution time of a function using a decorator."""
import time
import math

def factorial_number(f):
    def inner(*args,**kwargs):
        # storing time before function execution
            begin_time = time.time()
            f(*args,**kwargs)

            end_time = time.time()
            print("Total time taken in : ", f.__name__, end_time - begin_time)
    return inner

@factorial_number
def factorial(n):
    time.sleep(2)
    print(math.factorial(n))

num = int (input())
#for i in range(1,10):
factorial(num)