"""Write a Python program to get the maximum and minimum value in a dictionary."""

d = {'ravi':'10','rajnish':'9','sanjeev':'15','yash':'2','suraj':'32','neha':'7','harsh':'25'}
m = max(map(int,d.values()))
m1 = min(map(int,d.values()))
print(m,m1)