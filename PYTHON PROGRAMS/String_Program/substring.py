string = str(input("Enter the string"))
string1 = str(input("Enter substring"))

try:
    string.index(string1)
except ValueError:
    print("Not Found")
else:
    print("Found")