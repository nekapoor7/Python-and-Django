"""Write a Python function that takes a list of words and returns the length of the longest one. """

s = ["alpha","omega","up","down","over","under","purple","red","blue","green"]
ss = sorted(s,key=len)
print(len(s))
print(ss[0])
print(ss[-1])
