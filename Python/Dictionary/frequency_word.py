"""Python Program to Count the Frequency of Words Appearing in a String Using a Dictionary"""

from collections import Counter

text = input()

occur = Counter(text)
print(occur)

Count = Counter([a for a in text.split()])
print(Count)