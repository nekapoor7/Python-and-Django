string1 = str(input())
str1 = str(input())

try:
    string1.index(str1)
except ValueError:
    print("Not Found")
else:
    print("Found")