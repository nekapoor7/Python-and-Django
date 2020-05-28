"""Write a Python script to check whether a given key already exists in a dictionary. """

d = {'ravi':'10','rajnish':'9','sanjeev':'15','yash':'2','suraj':'32','neha':'7','harsh':'25'}
k = input()
if k in d:
    print("Key Exist",d[k])
else:
    print("Key Missing")