"""Write a Python program to count repeated characters in a string. Go to the editor
Sample string: 'thequickbrownfoxjumpsoverthelazydog'
Expected output :
o 4
e 3
u 2
h 2
r 2
t 2"""
from collections import Counter
s = str(input())
s1 = Counter(s)
d = dict(s1)
d1 = {}

for key,value in d.items():
    if value > 1:
        d1.update({key:value})
print(d1)

