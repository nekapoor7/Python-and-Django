my_dict = {}

limit = int(input("Enter the limit"))

for i in range(limit):
    key = input("Enter the keys :")
    value = input("Enter the values")
    my_dict.update({key:value})
print(my_dict)

search = int(input("Enter the key to be searched"))

if search in my_dict:
    print("Key is present")
else:
    print("Key is not present")
