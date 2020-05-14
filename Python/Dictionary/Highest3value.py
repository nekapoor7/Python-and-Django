"""Write a Python program to find the highest 3 values in a dictionary."""
from collections import Counter
d = {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81, 10: 100, 11: 121, 12: 144, 13: 169, 14: 196, 15: 225}
N = int(input())
dd = dict(Counter(d).most_common(N))
print(dd)

