"""Python | Sort Python Dictionaries by Key or Value"""

from collections import OrderedDict

dict_1 = {'ravi':'10','rajnish':'9','sanjeev':'15','yash':'2','suraj':'32'}

key_dict = OrderedDict(sorted(dict_1.items()))


print(key_dict)
value_int = dict((key,int(value)) for key,value in dict_1.items())

sort_value =sorted(value_int.items(),key=lambda x:x[1])
print(sort_value)