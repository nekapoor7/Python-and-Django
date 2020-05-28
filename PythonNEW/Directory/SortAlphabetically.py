"""Write a Python program to sort a list alphabetically in a dictionary."""

d = {'ravi':'10','rajnish':'9','sanjeev':'15','yash':'2','suraj':'32','neha':'7','harsh':'25'}
dd = sorted(d,key=str.lower)
print(dd)
