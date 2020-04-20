string = str(input("Enter the string"))
ch = str(input("Enter the character"))
new_string = str(input("Enter the string"))

str2 = ''
for i in range(len(string)):
    if(string[i] == ch):
        str2 = str2 + new_string
    else:
        str2 = str2 + string[i]
print("\nOriginal String :  ", string)
print("Modified String :  ", str2)
