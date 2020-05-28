"""Write a Python program to count the occurrences of each word in a given sentence."""
from collections import Counter
s = input()
ss = Counter(s.split())
print(ss)