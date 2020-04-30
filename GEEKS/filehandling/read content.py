"""Python Program to Read the Contents of a File"""

with open("C:\\Users\\nekapoor\\git\\Python-and-Django\\PYTHON PROGRAMS\\file_data\\data.txt",'r',encoding='utf-8') as file1:
    for line in file1.read():
        print(line,end='')


"""Python Program to Count the Number of Words in a Text File"""

with open("C:\\Users\\nekapoor\\git\\Python-and-Django\\PYTHON PROGRAMS\\file_data\\data.txt", 'r') as f:
    data = f.read()
    line = data.splitlines()
    words = data.split()
    spaces = data.split(" ")
    charc = (len(data) - len(spaces))

    print('\n Line number ::', len(line), '\n Words number ::', len(words), '\n Spaces ::', len(spaces),
          '\n Charecters ::', (len(data) - len(spaces)))


"""Python Program to Count the Occurrences of a Word in a Text File"""

print(open("C:\\Users\\nekapoor\\git\\Python-and-Django\\PYTHON PROGRAMS\\file_data\\data.txt", 'r').read().count(input()))


"""Python Program to Count the Occurrences of Each  Word in a Text File"""

from string import ascii_lowercase
from collections import Counter

with open("C:\\Users\\nekapoor\\git\\Python-and-Django\\PYTHON PROGRAMS\\file_data\\data.txt", 'r') as f:
    print(Counter(letter for line in f for letter in line.lower() if letter in ascii_lowercase))