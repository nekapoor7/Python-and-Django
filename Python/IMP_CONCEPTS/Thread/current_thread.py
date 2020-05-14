"""Set and Get Thread Name

1. current_thread() : This function returns the current thread object.
2. getName() : To get the name of thread we use this method.
3. setName(name) : Use to set the name of the thread.
4. name Property : Use to get or set name of the thread.
"""


from threading import Thread,current_thread

def display():
    print("Child Thread",current_thread())
    print("Child Thread", current_thread().getName())
    current_thread().setName('Neha')
    print("Child Thread", current_thread().getName())

t= Thread(target=display)
t1 = Thread(target=display)
t.start()
t1.start()

print("Main Thread",current_thread())
print("Main Thread",current_thread().getName())
current_thread().setName('Harsh')
print("Child Thread", current_thread().getName())