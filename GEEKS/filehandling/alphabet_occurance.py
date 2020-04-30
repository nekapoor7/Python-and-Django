"""Python Program to Count the Occurrences of each alphabet in a Text File"""
from string import ascii_letters
from collections import Counter

with open("C:\\Users\\nekapoor\\git\\Python-and-Django\\PYTHON PROGRAMS\\file_data\\data.txt",'r',encoding='utf-8') as f:
    print(Counter(letter for line in f for letter in line.lower() if letter in ascii_letters))