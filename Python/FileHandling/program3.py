"""Counting the number of occurrences of a word in a text file"""
from collections import Counter

with open("C:\\Users\\nekapoor\\git\\Python-and-Django\\PYTHON PROGRAMS\\file_data\\data.txt",'r',encoding='utf-8') as f:
    data = f.read()
    print(data)

    c = Counter()
    for line in data.splitlines():
        c.update(line.split())
        dict1 = dict(c)
    print(c)
    print(type(c))
    print(dict1)
