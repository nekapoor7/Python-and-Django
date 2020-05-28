"""Write a Python program to check whether a list contains a sublist"""

a = [3,7]
b = [2,4,3,5,7]
if all(i in b for i in a):
    print(True)
else:
    print(False)