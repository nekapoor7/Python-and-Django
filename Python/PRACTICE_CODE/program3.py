"""Python Program to Check if a Given Key Exists in a Dictionary or Not"""

dict1 = {'a': 10, 'b': 8}
dict2 = {'d': 6, 'c': 4}

res = {**dict1,**dict2}
print(type(res))
key = input()

if key in res:
    print("Key Found")
else:
    print("Key Not Found")

