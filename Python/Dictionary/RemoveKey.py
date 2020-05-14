"""Write a Python program to remove a key from a dictionary."""

d = {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81, 10: 100, 11: 121, 12: 144, 13: 169, 14: 196, 15: 225}

d1 = [int(x) for x in input().split()]

d2 = {key: value for key,value in d.items() if key not in d1}
print(d2)

d3 = {'ravi':'10','rajnish':'9','sanjeev':'15','yash':'2','suraj':'32','neha':'7','harsh':'25'}

dd = [str(x) for x in input().split()]

dic = {key : value for key,value in d3.items() if key not in dd}

print(dic)