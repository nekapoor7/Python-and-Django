mydict = {}
limit = int(input())

for i in range(limit):
    key = input()
    value = input()
    mydict.update({key:value})
    print(mydict)

key_removal = tuple()