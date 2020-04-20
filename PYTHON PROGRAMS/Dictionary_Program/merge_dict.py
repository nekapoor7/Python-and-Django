def merge_list(my_dict,my_dict1):
    result = {**my_dict, **my_dict1}
    return result

my_dict = {}
my_dict1 = {}

limit = int(input("Enter the limit"))
limit1 = int(input("Enter the limit"))
for i in range(limit):
    key = input("Enter the keys :")
    value = input("Enter the values")
    my_dict.update({key:value})
print(my_dict)

for i in range(limit1):
    key = input("Enter the keys :")
    value = input("Enter the values")
    my_dict1.update({key:value})
print(my_dict1)
my_dict2 = merge_list(my_dict,my_dict1)
print(my_dict2)

total = 1

for i in my_dict2:
    total = total * my_dict2[i]

print(total)



