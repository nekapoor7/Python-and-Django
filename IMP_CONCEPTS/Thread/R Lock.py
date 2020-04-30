"""R Lock
A Re Entrant lock is a synchronization primitive that may be acquired by multiple times by the same thread.

The standard lock doesn't know which thread is currently holding the lock, if lock is held, any thread that attempts
to acquire it will block, even if the same thread itself is already holding the lock. in such cases, R Lock(Re-Entrant)
lock is used.

A Re Entrant lock must be released by the thread that acquired it. Once a thread has acquired a Re Entrant lock,
the same thread may acquire it again without blocking, the thread must release it once for each time is
has acquired it.

"""
from threading import *

class Flight:

    def __init__(self,available_seat):
        self.available_seat = available_seat
        self.l = RLock()
        #print(self.l)

    def reserve(self,need_seat):
        self.l.acquire(blocking=True,timeout=-1)
        self.l.acquire(blocking=True, timeout=-1)
        #print(self.l)
        print("Available Seat",self.available_seat)
        if self.available_seat >= need_seat:
            name = current_thread().name
            print(f'{need_seat} seat is allocated for {name}')
            self.available_seat -= need_seat
        else:
            print("All seats have allocated")
        self.l.release()
        self.l.release()

f = Flight(2)
t1 = Thread(target=f.reserve, args=(1,), name='Rahul')
t2 = Thread(target=f.reserve, args=(1,), name='Sonam')
t3 = Thread(target=f.reserve, args=(1,), name='Raj')
t1.start()
t2.start()
t3.start()