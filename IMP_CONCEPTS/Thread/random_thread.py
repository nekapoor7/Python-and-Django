import threading
import time
import random
def Thread_execution(i):
    print("Execution of thread {} started".format(i))
    sleepTime = random.randint(1,4)
    time.sleep(sleepTime)
    print("Execution of thread {} finished".format(i))

for i in range(4):
    thread = threading.Thread(target=Thread_execution,args=(i,))
    thread.start()
    print("Active threads:", threading.enumerate())