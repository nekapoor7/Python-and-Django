from collections import OrderedDict

dict_1 = {'ravi':'10','rajnish':'9','sanjeev':'15','yash':'2','suraj':'32','neha':'32'}

dict1 = OrderedDict(sorted(dict_1.items()))
print(dict1)

dict2 = dict((key,int(value)) for key,value in dict_1.items())
print(dict2)
a = sorted(dict2.items(),key=lambda x:x[1])
print(a)