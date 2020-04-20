import threading
import time

def nondaemonThread():
    print("Starting thread")
    time.sleep(8)
    print("Exiting Thread")

def daemonThread():
    while True:
        print("Hello")
        time.sleep(2)

if __name__ == '__main__':
    nondaemonThread = threading.Thread(target=nondaemonThread)
    daemonThread = threading.Thread(target=daemonThread)
    daemonThread.setDaemon(True)
    daemonThread.start()
    nondaemonThread.start()