""" Creating a thread by creating a child class to Thread Class

We can create our own thread child class by inheriting  Thread Class from threading module.

Threading Class Methods

1. start() : Once a thread is created it should be started by calling start() Method
2. run() : Every thread will run this method when thread is started. A thread will automatically terminates when it comes out
of the run() method.
3. join() : This method is used to wait till the thread completely executes the run() method"""

from threading import Thread

class Mythread(Thread):
    def run(self):
        for i in range(5):
            print("Child thread")

t = Mythread()
t.start()
for i in range(5):
        print("Main Thread")