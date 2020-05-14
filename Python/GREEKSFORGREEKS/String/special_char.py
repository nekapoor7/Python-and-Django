# Python program to check if a string
# contains any special character

import re

def specialchar(string):
    regex = re.compile('[@_!#$%^&*()<>?/\|}{~:]')

    if regex.search(string) == None:
        return "String is accepted"

    else:
        return "String is not accepted."

string = input()
print(specialchar(string))