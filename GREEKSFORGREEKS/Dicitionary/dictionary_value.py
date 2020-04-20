my_dict={}

limit = int(input())

for i in range(limit):
    key = input()
    item = input()
    my_dict.update({key:item})
print(my_dict)

#dict_value = {k: v for k, v in sorted(my_dict.values(), key=lambda item: item[1])}

a = sorted(my_dict.items(), key=lambda x: x[1])
print(a)
