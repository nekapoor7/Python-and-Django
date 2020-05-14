"""Write a Python program to count the number of lines in a text file."""
from collections import Counter
with open("C:\\Users\\nekapoor\\git\\Python-and-Django\\PYTHON PROGRAMS\\file_data\\nehacopy.txt", 'r',
              encoding='utf-8') as f:
        data = f.read()
        lines = data.splitlines()
        words = data.split()
        spaces = data.split(" ")
        charc = (len(data) - len(spaces))
        w_occur = Counter(data.split())
        c_occur = Counter(data)

        print("Number of Lines",len(lines))
        print("Number of Words", len(words))
        print("Number of Spaces", len(spaces))
        print("Number of Characters", charc)
        print(w_occur)
        print(c_occur)

print(open("C:\\Users\\nekapoor\\git\\Python-and-Django\\PYTHON PROGRAMS\\file_data\\nehacopy.txt", 'r').read().count(input()))