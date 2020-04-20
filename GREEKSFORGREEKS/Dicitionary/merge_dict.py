import collections

mydict = {}
mydict1 = {}
merge_dict = {}
limit = int(input())

for i in range(limit):
    key = input()
    item = input()
    mydict.update({key:item})
print(mydict)

limit1 = int(input())

for i in range(limit1):
    key = input()
    item = input()
    mydict.update({key: item})
print(mydict1)

merge_dict = {**mydict,**mydict1}
print(merge_dict)

dict_with_int = dict((k, int(v)) for k, v in merge_dict.items())
sum = 0

for i in dict_with_int:
    sum = sum + dict_with_int[i]
print(sum)

dict_sort_key = collections.OrderedDict(sorted(merge_dict.items()))
print(dict_sort_key)

