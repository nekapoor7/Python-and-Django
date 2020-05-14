"""Python Program to Check if a Given Key Exists in a Dictionary or Not"""

dict1 = {'ravi':'10','rajnish':'9','sanjeev':'15','yash':'2','suraj':'32','neha':'7','harsh':'25'}
key = input()

if key in dict1:
    print("Key Exists")
else:
    print("Key Not Exists")