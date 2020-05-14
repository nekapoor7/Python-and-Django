""" Write a Python program to check multiple keys exists in a dictionary."""

d = {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81, 10: 100, 11: 121, 12: 144, 13: 169, 14: 196, 15: 225}
dd = [int(x) for x in input().split()]
if {key:value for key,value in d.items() if key in dd}:
    print("Key Exists")
else:
    print("Key Not Exists")
