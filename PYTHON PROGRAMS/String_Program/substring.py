"""Python | Check if a Substring is Present in a Given String"""

string1 = str(input())
string2 = str(input())
result = [val for val in string2 if val in string1]
var = ''.join(result)

if var in string1:
    print("Found")
else:
    print("Not Found")

