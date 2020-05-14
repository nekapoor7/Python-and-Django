mydict = {}
limit = int(input())

for i in range(limit):
    key = input()
    value = input()
    mydict.update({key:value})

print(mydict)

new_dict = {}

key_removal = [str(x) for x in input().split()]

new_dict = {key: val for key,val in mydict.items() if key not in key_removal}

print(new_dict)

