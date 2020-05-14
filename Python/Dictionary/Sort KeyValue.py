"""Python | Sort Python Dictionaries by Key or Value"""


dict1 = {'ravi':'10','rajnish':'9','sanjeev':'15','yash':'2','suraj':'32','neha':'7','harsh':'25'}

""" SORT BY KEYS"""
from collections import OrderedDict

result = OrderedDict(sorted(dict1.items()))

print(result)


"""SORT BY VALUES"""

dict2 = dict((key,int(value))for key,value in dict1.items())

values = sorted(dict2.items(),key=lambda x:x[1])

print(values)

