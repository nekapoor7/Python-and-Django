"""Write a Python program to find the maximum occurring character in a given string."""

from collections import Counter
s = ['aaa', 'bbb', 'ccc', 'bbb', 'aaa', 'aaa']
m = Counter(s)
print(m.most_common()[0][0])
print(m.most_common()[1][0])