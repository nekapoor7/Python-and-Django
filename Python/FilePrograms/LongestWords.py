"""Write a python program to find the longest words. """

from functools import reduce

with open("C:\\Users\\nekapoor\\git\\Python-and-Django\\PYTHON PROGRAMS\\file_data\\nehacopy.txt", 'r',
              encoding='utf-8') as f:
    s = [y for x in f.readlines() for y in x.split()]
    longest = reduce(lambda x, y: y if len(x) < len(y) else x, s, "")
    print("The longest word is", longest, "and it is", len(longest), "characters long")
