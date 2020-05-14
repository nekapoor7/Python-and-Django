"""Write a Python script to check whether a given key already exists in a dictionary."""

d = {'ravi':'10','rajnish':'9','sanjeev':'15','yash':'2','suraj':'32','neha':'7','harsh':'25'}
key = input()
if key in d:
    print("Key exist",d[key])
else:
    print("Key not exist")
