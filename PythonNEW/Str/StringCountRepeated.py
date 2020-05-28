"""Write a Python program to count repeated characters in a string. Go to the editor
Sample string: 'thequickbrownfoxjumpsoverthelazydog'
Expected output :
o 4
e 3
u 2
h 2
r 2
t 2"""
'''from collections import Counter
s = input()
ss = Counter(s)
print(ss)'''

import collections
s = input()
d = collections.defaultdict(int)
for c in s:
    d[c] += 1
d = {key:value for key,value in d.items() if value > 1}
print(d)
