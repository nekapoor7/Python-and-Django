string = str(input("Enter the string "))
string1 = ''

for i in range(len(string)):
    if(string[i] >= 'a' and string[i] <='z'):
        string1 = string1 + chr((ord(string[i]) -32))
    else:
        string1 = string1 + string[i]

print("\nOriginal String in Lowercase  =  ", string)
print("The Given String in Uppercase =  ", string1)
