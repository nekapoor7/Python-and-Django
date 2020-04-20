''' threading_run_background_deco2.py
apply threading to a function with a function decorator
to allow it to run in the background
tested with Python27 and Python33  by  vegaseat  27jun2014
'''
import time
import threading
def background(f):
    '''
    a threading decorator
    use @background above the function you want to run in the background
    '''
    def bg_f(*a, **kw):
        threading.Thread(target=f, args=a, kwargs=kw).start()
    return bg_f
@background
def counter(name, n):
    """show the count every second"""
    for k in range(1, n+1):
        print("{} counts {}".format(name, k))
        time.sleep(1)
# start the counters
# note that with the @background decorator
# Frank and Doris count simultaneously
# note from SOS: Frank may not always count first
counter("Frank", 5)
counter("Doris", 5)