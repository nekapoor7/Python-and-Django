"""Write a Python program to get the key, value and item in a dictionary."""
d = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}
print("key value count")
for count,(key,value) in enumerate(d.items(),1):
    print(key,' ',value,' ',count)

"""Write a Python program to sort Counter by value. Go to the editor
Sample data : {'Math':81, 'Physics':83, 'Chemistry':87}
Expected data: [('Chemistry', 87), ('Physics', 83), ('Math', 81)]"""
from collections import OrderedDict
from operator import itemgetter
l = {'Math':81, 'Physics':83, 'Chemistry':87}
ll = OrderedDict(sorted(l.items(),key=itemgetter(1),reverse=True))
print(ll)

""" Write a Python program to create a dictionary from two lists without losing duplicate values. Go to the editor
Sample lists: ['Class-V', 'Class-VI', 'Class-VII', 'Class-VIII'], [1, 2, 2, 3]
Expected Output: defaultdict(<class 'set'>, {'Class-VII': {2}, 'Class-VI': {2}, 'Class-VIII': {3}, 'Class-V': {1}})"""
