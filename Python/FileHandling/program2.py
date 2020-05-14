"""Python Program to Count the Number of Words in a Text File
Python Program to Count the Number of Lines in a Text File
Python Program to Count the Number of Blank Spaces in a Text File"""


with open("C:\\Users\\nekapoor\\git\\Python-and-Django\\PYTHON PROGRAMS\\file_data\\data.txt",'r',encoding='utf-8') as file1:
    data = file1.read()
    line = data.splitlines()
    word = data.split()
    spaces = data.split(" ")
    char = (len(data) - len(spaces))

    print(len(line))
    print(len(word))
    print(len(spaces))
    print(char)

"""Python Program to Count the Occurrences of a Word in a Text File"""

word_occurance = open("C:\\Users\\nekapoor\\git\\Python-and-Django\\PYTHON PROGRAMS\\file_data\\data.txt").read().count(input())
print(word_occurance)

"""Python Program that Reads a Text File and Counts the Number of Times a Certain Letter Appears in the Text File"""

from string import ascii_letters
from collections import Counter

with open("C:\\Users\\nekapoor\\git\\Python-and-Django\\PYTHON PROGRAMS\\file_data\\data.txt",'r',encoding='utf-8') as f:
    print(Counter(letter for line in f for letter in line.lower() if letter in ascii_letters))

