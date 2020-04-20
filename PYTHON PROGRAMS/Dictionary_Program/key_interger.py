my_dict = {}

limit = int(input("Enter the limit"))

for i in range(limit):
    key = input("Enter the keys :")
    value = input("Enter the values")
    my_dict.update({key:value})
print(my_dict)
print(type(my_dict))

# printing original list
print ("The original list is : " + str(my_dict))

for dict in my_dict:
    for key in dict:
        dict[key] = int(dict[key])
# printing result
print ("The modified converted list is : " +  str(my_dict))