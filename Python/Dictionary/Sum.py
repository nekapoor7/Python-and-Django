"""Python program to find the sum of all items in a dictionary"""

dict1 = {'ravi':'10','rajnish':'9','sanjeev':'15','yash':'2','suraj':'32','neha':'7','harsh':'25'}

dict2 = dict((key,int(value))for key,value in dict1.items())

print(sum(dict2.values()))