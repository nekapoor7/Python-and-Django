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