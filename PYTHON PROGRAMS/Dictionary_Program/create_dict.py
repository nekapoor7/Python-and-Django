my_dict = {}

limit = int(input("Enter the limit"))

for i in range(limit):
    key = input("Enter the keys :")
    value = input("Enter the values")
    my_dict.update({key:value})
print(my_dict)

