"""Write a Python program to sum all the items in a dictionary."""

d = {'ravi':'10','rajnish':'9','sanjeev':'15','yash':'2','suraj':'32','neha':'7','harsh':'25'}
d1 = {key:int(value) for key,value in d.items()}
print(sum(d1.values()))

d2 = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}
print(sum(d2.values()))
sum = 0
for key in d2:
    sum = sum + d2[key]
print(sum)

"""Write a Python program to multiply all the items in a dictionary."""

d2 = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}
m = 1
for key in d2:
    m = m * d2[key]
print(m)