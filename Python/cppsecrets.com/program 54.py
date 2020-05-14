"""Python Program to Determine How Many Times a Given Letter Occurs in a String Recursively"""
import re

text = input()
character = input()

letteroccur = (val for val in character if val in text)

letter = ''.join(letteroccur)

if letter in text:
    print(len(letter))
else:
    print("It doesn't contain")