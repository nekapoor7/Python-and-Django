"""Write a Python program to get a dictionary from an object's fields."""

class Dictionary:
    def __init__(self):
        self.red = 1
        self.green = 2
        self.blue = 3

    def print(self):
        pass

obj = Dictionary()
print(obj.__dict__)

"""Write a Python program to remove duplicates from Dictionary. """
d = {'a': 400, 'b': 400, 'd': 400, 'c': 300}
r = {}
for key,value in d.items():
    if value not in r.values():
        r[key] = value
print(r)

"""Write a Python program to combine two dictionary adding values for common keys. Go to the editor
d1 = {'a': 100, 'b': 200, 'c':300}
d2 = {'a': 300, 'b': 200, 'd':400}
Sample output: Counter({'a': 400, 'b': 400, 'd': 400, 'c': 300})"""
from collections import Counter
d1 = Counter({'a': 100, 'b': 200, 'c':300})
d2 = Counter({'a': 300, 'b': 200, 'd':400})
res = d1 + d2
print(res)

"""Write a Python program to print all unique values in a dictionary. Go to the editor
Sample Data : [{"V":"S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII":"S005"}, {"V":"S009"},{"VIII":"S007"}]
Expected Output : Unique Values: {'S005', 'S002', 'S007', 'S001', 'S009'}"""
d = [{"V":"S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII":"S005"}, {"V":"S009"},{"VIII":"S007"}]
