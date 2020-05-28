"""Write a Python program to find the highest 3 values in a dictionary. """
from collections import Counter
d = {'ravi':'10','rajnish':'9','sanjeev':'15','yash':'2','suraj':'32','neha':'7','harsh':'25'}
dd = {key:int(value) for key,value in d.items()}
N = int(input())
print(dict(Counter(dd).most_common(N)))
