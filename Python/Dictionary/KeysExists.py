"""Python Program to Check if a Given Key Exists in a Dictionary or Not"""

d = {'ravi':'10','rajnish':'9','sanjeev':'15','yash':'2','suraj':'32','neha':'7','harsh':'25'}

nkeys = input()

if nkeys in d:
    print("Key Exist")
else:
    print("Key not Exist")