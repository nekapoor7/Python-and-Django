""" Thread Synchronization

Many threads trying to access the same object can lead the problems like making data inconsistent
or getting unexpected output. So When a thread is already accessing an object, preventing any other thread
accessing the same object is called Thread Synchronization.

The object on which the threads are synchronized is called Synchronized Object or Mutually
Exclusive Lock(mutex).

Thread Synchronization is recommended when multiple threads are acting on the same object simultaneously.

There are following techniques to do thread synchronization:
1. using locks
2. using R locks (Re-Entrant Lock)
3. Semaphores

1 Using Locks :
Locks are typically used to synchronize access to a shared resource. Lock can be used to lock the object in which
the thread is acting. A lock has 2 states, locked and unlocked. It is created in the unlocked state.

There are 2 methods : acquire() and release()
1. acquire() : this method is used to change the state to locked and returns immediately. When the state is locked,
acquire() blocks until a call to release() in another thread changes it to unlocked, then the acquire() call resets it to
locked and returns.

Syntax : acquire(blocking = True, timeout = -1)
True -> it blocks until the lock is unlocked, then set it to locked and return True.
False -> it does not block.
Timeout = -1 specify unbounded wait, it will wait until and unless it will release if any positive number is given
it specify the seconds for which thread is block as soon as time over it will allow next thread to work.

2. release() : This method is used to release the lock. This can be called from any thread, not only the thread which
has acquired the lock.

When the lock is locked,reset it to unlocked and return. If any other threads are blocked waiting for the lock
to become unlocked, allow exactly one of them to proceed.
When invoked on an unlocked lock, a Runtime Error is raised.
"""
from threading import *

class Flight:

    def __init__(self,available_seat):
        self.available_seat = available_seat
        self.l = Lock()

    def reserve(self,need_seat):
        self.l.acquire(blocking=False)
        print("Available Seat",self.available_seat)
        if self.available_seat >= need_seat:
            name = current_thread().name
            print(f'{need_seat} seat is allocated for {name}')
            self.available_seat -= need_seat
        else:
            print("All seats have allocated")
        self.l.release()
f = Flight(2)
t1 = Thread(target=f.reserve,args=(1,),name='Rahul')
t2 = Thread(target=f.reserve,args=(1,),name='Sonam')
t3 = Thread(target=f.reserve,args=(1,),name='Raj')
t1.start()
t2.start()
t3.start()




