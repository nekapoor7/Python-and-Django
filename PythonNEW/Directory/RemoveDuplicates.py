"""Write a Python program to remove duplicates from Dictionary"""

d = {'a': 400, 'b': 400, 'd': 400, 'c': 300}
r = {}

for key,value in d.items():
    if value not in r.values():
        r[key] = value
print(r)
