#Remove all duplicates from a given string in Python
from collections import OrderedDict


def removechar(s):

    return "".join(OrderedDict.fromkeys(s))


s = input()
print(removechar(s))

