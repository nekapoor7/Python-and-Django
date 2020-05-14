mydict={}
limit = int(input())

for i in range(limit):
    key = input()
    item = int(input())
    mydict.update({key:item})
print(mydict)


sum = 0
for i in mydict:
    sum = sum + mydict[i]
print(sum)