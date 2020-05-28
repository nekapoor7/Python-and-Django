"""Write a Python program to multiply all the items in a dictionary."""

d = {'ravi':'10','rajnish':'9','sanjeev':'15','yash':'2','suraj':'32','neha':'7','harsh':'25'}
d1 = {key:int(value) for key,value in d.items()}
total = 1

for key in d1:
    total = total * d1[key]
print(total)