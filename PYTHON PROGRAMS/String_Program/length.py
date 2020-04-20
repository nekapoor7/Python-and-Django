#Python Program to Calculate the Length of a String Without Using a Library Function

def length_string(string):
    count = 0
    for i in string:
        count += 1
    return count

string= str(input("Enter the string"))
print("Length of the string",length_string(string))

