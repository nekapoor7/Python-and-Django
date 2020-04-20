# Python3 code to demonstrate
# Type conversion in list of dicts.
# using naive method

# initializing list of dictionary
test_list = [{'a': '1', 'b': '2'}]
#print(type(test_list))

# printing original list
print("The original list is : " + str(test_list))
print(type(test_list))

# using naive method
# type converstion in list of dicts.
for dicts in test_list:
    for keys in dicts:
        dicts[keys] = int(dicts[keys])

    # printing result
print("The modified converted list is : " + str(test_list))
