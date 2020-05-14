"""Python | Merging two Dictionaries"""

d1 = {'a': 10, 'b': 20, 'c': 30}
d2 = {'b': 200, 'd': 400}

d3 = {**d1,**d2}
print(d3)