"""Python | Ways to remove a key from dictionary"""

dict1 = {'ravi':'10','rajnish':'9','sanjeev':'15','yash':'2','suraj':'32','neha':'7','harsh':'25'}

dict2 = {}

key_removal = [str(x) for x in input().split()]

dict2 = {key:value for key,value in dict1.items() if key not in key_removal}

print(dict2)