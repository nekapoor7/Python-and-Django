import time
import threading

def calcu_square(list1):
    print("Calculate square")
    for i in list1:
        time.sleep(0.2)
        print(i*i)

def calcu_cube(list1):
    print("Calculate Cube")
    for i in list1:
        time.sleep(0.2)
        print(i*i*i)

N = int(input())
list1 = list(map(int,input().split()))
t = time.time()
t1 = threading.Thread(target=calcu_square,args=(list1,))
t2 = threading.Thread(target=calcu_cube,args=(list1,))

t1.start()
t2.start()

t1.join()
t2.join()

print(time.time()-t)

