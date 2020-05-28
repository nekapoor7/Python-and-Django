"""Write a Python program to multiply all the items in a dictionary."""

d = {'ravi':'10','rajnish':'9','sanjeev':'15','yash':'2','suraj':'32','neha':'7','harsh':'25'}
d1 = {key:int(value) for key,value in d.items()}
#d1 = {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81, 10: 100, 11: 121, 12: 144, 13: 169, 14: 196, 15: 225}
total = 1

for i in d1:
    total = total * d1[i]
print(total)