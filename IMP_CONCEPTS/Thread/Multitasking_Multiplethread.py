"""Multitasking using Multiple Thread

When multiple tasks are executed at a time, Then it is called Multitasking.For this purpose we need more than one thread,
 we have used more than one thread , it is called Multithreading."""

from threading import Thread

class Hotel:

    def __init__(self,t):
        self.t = t

    def food(self):
        for i in range(1,6):
            print(self.t,i)

h1 = Hotel("Take Order ")
h2 = Hotel("Surve Order ")

t1 = Thread(target=h1.food)
t2 = Thread(target=h2.food)

t1.start()
t2.start()