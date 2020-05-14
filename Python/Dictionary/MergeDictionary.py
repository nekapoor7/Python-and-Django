"""Write a Python script to merge two Python dictionaries."""
from collections import Counter
dic1 = Counter({'A': 25, 'B': 41, 'C': 32})
dic2 = Counter({'A': 21, 'B': 12, 'C': 62})

d = dic1 + dic2
print(dict(d))
