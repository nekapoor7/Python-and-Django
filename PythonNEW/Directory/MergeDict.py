"""Write a Python script to merge two Python dictionaries."""

d1 = {'a': 100, 'b': 200, 'c':300}
d2 = {'a': 300, 'b': 200, 'd':400}
d = d1.update(d2)
print(d)