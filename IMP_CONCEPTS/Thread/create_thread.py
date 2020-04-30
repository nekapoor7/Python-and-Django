""" Multitasking Executing multiple task at the same time."""

""" There are two types of Multitasking 
1. Process based Multitasking
2. Thread based Multitasking
1. Process based Multitasking: Executing multiple task at the same time where each task is a separate 
independent program (process),is called process based multitasking. It is suitable for Operating System Level.

2. Thread based Multitasking: Executing multiple task at the same time where each task is a separate independent 
part of the same program(process), is called Thread based multitasking and each independent part is called Thread.
It is suitable for programmatic level"""

"""Thread is a separate flow of execution.Every thread has a task.

Multithreading: Using multiple threads in a program or process."""

"""Main Thread: When we start any Python Program, one thread begins running immediately, which is called Main Thread of 
that program created by Python Virtual Machine(PVM).

The main thread is created automatically when your program is started.

################## Creating a Thread ################################################

Thread class of threading module is used to create threads. To create our own thread we need to create an object of 
Thread Class.

Thread can be creating by following ways:
1. Can be created without using a class
2. Can be created via child class to Thread Class
3. Can be created without child class to Thread Class.

Once a thread is created it should be started by calling start() Method."""


import threading

def add(a,b):
    result = a + b
    print("Thread Running",result)

for i in range(5):
    t = threading.Thread(target=add, args=(10, 20))
    t.start()