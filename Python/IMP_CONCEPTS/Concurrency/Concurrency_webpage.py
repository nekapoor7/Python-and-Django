import urllib.request

import time

ts = time.time()

req = urllib.request.urlopen('http://www.tutorialspoint.com')

pageHtml = req.read()

te = time.time()

print("Page Fetching time : {} Seconds".format(te-ts))