"""Write a Python program to compute the similarity between two lists. Go to the editor
Sample data: ["red", "orange", "green", "blue", "white"], ["black", "yellow", "green", "blue"]
Expected Output:
Color1-Color2: ['white', 'orange', 'red']
Color2-Color1: ['black', 'yellow']"""
'''
l= ["red", "orange", "green", "blue", "white"]
l1 = ["black", "yellow", "green", "blue"]

setA = set(l)
setB = set(l1)

Color1Color2 = list(setA.difference(setB))
Color2Color1 = list(setB.difference(setA))

print(Color1Color2)
print(Color2Color1)'''

from collections import Counter
l= ["red", "orange", "green", "blue", "white"]
l1 = ["black", "yellow", "green", "blue"]

C1 = Counter(l)
C2 = Counter(l1)

print(list(C1-C2))
print(list(C2-C1))
