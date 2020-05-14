"""Python Program to Sum All the Items in a Dictionary"""

dict_1 = {'ravi':'10','rajnish':'9','sanjeev':'15','yash':'2','suraj':'32'}

d = dict((key,int(value)) for key,value in dict_1.items())

sum = 0
for i in d:
    sum = sum + d[i]
print(sum)