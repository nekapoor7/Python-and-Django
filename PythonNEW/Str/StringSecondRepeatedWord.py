"""Write a Python program to find the second most repeated word in a given string. """
from collections import Counter
def secondFrequent(input):
    dict = Counter(input)
    value = sorted(dict.values(), reverse=True)
    secondLarge = value[1]

    for (key, val) in dict.items():
        if val == secondLarge:
            return key

print(secondFrequent(['aaa', 'bbb', 'ccc', 'bbb', 'aaa', 'aaa']))