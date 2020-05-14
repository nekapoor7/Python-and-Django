"""Write a Python program to remove duplicates from Dictionary. """

d = {'a': 400, 'b': 400, 'd': 400, 'c': 300}

result = {}
for key, value in d.items():
    if value not in result.values():
        result[key] = value
print(result)