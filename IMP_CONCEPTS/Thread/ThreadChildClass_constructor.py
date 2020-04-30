""" Thread Child Class with Constructor

"""

from threading import Thread

class MtThread(Thread):

    def __init__(self,a):
        Thread.__init__(self)
        print("Child thread Constructor",a)

    def run(self):
        pass

t = MtThread(10)
t.start()
print(
    "Main Thread"
)

########Creating a thread without creating a child class to thread Class############

"""We can create an indepenent thread child class that does not inherit from Thread Class from threading mpdule."""

from threading import Thread

class MyClass(object):

    def __init__(self,a,b):
        self.a = a
        self.b = b

    def add(self):
        return self.a + self.b

if __name__ == "__main__":
    myobj = MyClass(10,20)
    thobj = Thread(target=myobj.add,args=(10,20))
    thobj.start()

