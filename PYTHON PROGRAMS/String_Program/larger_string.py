'''from itertools import count

def largest_string(string1,string2):
    count1 = 0
    count2 = 0

    for i in string1:
        count1 = count1 + 1

        for j in string2:
            count2 = count2 + 1

    if (count1 < count2):
        print("Larger string is ",string2)

    elif (count1 == count2):
        print("Both strings are equal")

    else:
        print("Larger string is",string1)

string1 = str(input("Enter first string"))
string2 = str(input("Enter second string"))
largest_string(string1,string2)'''

import re

string1 = str(input("Enter first string"))
string2 = str(input("Enter second string"))

longest = len(max(re.findall(r'\w+',string1), key = len))
print(longest)