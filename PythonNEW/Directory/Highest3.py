"""Write a Python program to find the highest 3 values in a dictionary."""
from collections import Counter
d = {'item1': 45.50, 'item2':35, 'item3': 41.30, 'item4':55, 'item5': 24}
N = int(input())
dd = Counter(d).most_common(N)
print(dd)