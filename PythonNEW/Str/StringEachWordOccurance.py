"""Write a Python program to count the occurrences of each word in a given sentence. """
from collections import Counter
s = input()
s1 = Counter(s.split())
print(s1)