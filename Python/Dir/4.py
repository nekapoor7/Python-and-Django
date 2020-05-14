"""Write a Python program to create and display all combinations of letters,
selecting each letter from a different key in a dictionary. Go to the editor
Sample data : {'1':['a','b'], '2':['c','d']}
Expected Output:
ac
ad
bc
bd
Click me to see the sample solution"""
l = {'1':['a','b'], '2':['c','d']}


"""Write a Python program to find the highest 3 values in a dictionary. """
from collections import Counter
N = int(input())
d = {'ravi':'10','rajnish':'9','sanjeev':'15','yash':'2','suraj':'32','neha':'7','harsh':'25'}
dd = {key:int(value) for key,value in d.items()}
print(dict(Counter(dd).most_common(N)))

"""Write a Python program to combine values in python list of dictionaries. Go to the editor
Sample data: [{'item': 'item1', 'amount': 400}, {'item': 'item2', 'amount': 300}, {'item': 'item1', 'amount': 750}]
Expected Output: Counter({'item1': 1150, 'item2': 300})"""

"""Write a Python program to create a dictionary from a string. Go to the editor
Note: Track the count of the letters from the string.
Sample string : 'w3resource'
Expected output: {'3': 1, 's': 1, 'r': 2, 'u': 1, 'w': 1, 'c': 1, 'e': 2, 'o': 1}"""
s= 'w3resource'
k = Counter(s)
print(k)

"""Write a Python program to get the top three items in a shop. Go to the editor
Sample data: {'item1': 45.50, 'item2':35, 'item3': 41.30, 'item4':55, 'item5': 24}
Expected Output:
item4 55
item1 45.5
item3 41.3"""
d1 = {'item1': 45.50, 'item2':35, 'item3': 41.30, 'item4':55, 'item5': 24}
k1 = dict(Counter(d1).most_common(N))
print(k1)