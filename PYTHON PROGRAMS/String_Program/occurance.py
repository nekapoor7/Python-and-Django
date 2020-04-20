string = str(input("enter the string"))

res = {}

for keys in string:
    res[keys] = res.get(keys, 0) + 1

# printing result
print ("Count of all characters in GeeksforGeeks is : \n" + str(res))