"""Write a Python program to get the maximum and minimum value in a dictionary."""

d = {'ravi':'10','rajnish':'9','sanjeev':'15','yash':'2','suraj':'32','neha':'7','harsh':'25'}
dd = {key:int(value) for key,value in d.items()}

maxv = max(dd.values())
minv = min(dd.values())

print(maxv)
print(minv)

maxk = max(dd.keys())
print(maxk)
