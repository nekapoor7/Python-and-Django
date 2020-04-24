#Python Program to Count the Occurrences of a Word in a Text File

from collections import Counter

with open("C:\\Users\\nekapoor\\git\\Python-and-Django\\PYTHON PROGRAMS\\file_data\\data.txt",'r',encoding='utf-8') as file1:
    data = file1.read()
    print(data)

c = Counter()
for line in data.splitlines():
    c.update(line.split())
print(c)

