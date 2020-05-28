"""Write a Python program to sum all the items in a dictionary. """

d = {'a': 300, 'b': 200, 'c': 300, 'd': 400}
s = sum(d.values())
print(s)

d1 = {'ravi':'10','rajnish':'9','sanjeev':'15','yash':'2','suraj':'32','neha':'7','harsh':'25'}
s1 = sum(map(int,d1.values()))
print(s1)