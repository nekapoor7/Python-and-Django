"""Python program to find the sum of all items in a dictionary"""

dict_1 = {'ravi':'10','rajnish':'9','sanjeev':'15','yash':'2','suraj':'32'}

dict1_int = dict((key,int(value)) for key,value in dict_1.items())

sum = 0
for i in dict1_int:
    sum = sum + dict1_int[i]
print(sum)