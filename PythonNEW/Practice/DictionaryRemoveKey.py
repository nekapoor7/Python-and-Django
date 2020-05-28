"""Write a Python program to remove a key from a dictionary."""

d = {'ravi':'10','rajnish':'9','sanjeev':'15','yash':'2','suraj':'32','neha':'7','harsh':'25'}
keys = [str(x) for x in input().split()]
k = {key:int(value) for key,value in d.items() if key not in keys}
print(k)

