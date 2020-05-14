"""Python Program to Count the Occurrences of Each Word in a Given String Sentence"""

from collections import Counter

text = input()

occur = Counter(text)

print(occur)