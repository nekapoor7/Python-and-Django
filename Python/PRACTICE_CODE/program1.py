"""Python Program to Add a Key-Value Pair to the Dictionary"""
mydict={}
limit = int(input())

for i in range(limit):
    value = tuple(input())
    it = tuple(input())
    key = ','.join(value)
    item = ','.join(it)
    mydict.update({key:item})
print(mydict)