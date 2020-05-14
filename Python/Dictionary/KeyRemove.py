"""Python Program to Remove the Given Key from a Dictionary"""

d = {'ravi':'10','rajnish':'9','sanjeev':'15','yash':'2','suraj':'32','neha':'7','harsh':'25'}

key_remove = [str(x) for x in input().split()]

d1 = {key: value for key,value in d.items() if key not in key_remove}

print(d1)




