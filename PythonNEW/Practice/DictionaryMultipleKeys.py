"""Write a Python program to check multiple keys exists in a dictionary."""

d = {'item1': 45.50, 'item2':35, 'item3': 41.30, 'item4':55, 'item5': 24}
mkeys = [str(x) for x in input().split()]
if all(ele in d for ele in mkeys):
    print("Keys Exist")
else:
    print("Keys Missing")