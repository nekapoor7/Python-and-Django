"""Python Program to Calculate the Number of Upper Case Letters and Lower Case Letters in a String"""

import re

string1 = input()

lowercase = re.findall(r'[a-z]',string1)
uppercase = re.findall(r'[A-Z]',string1)

print(len(lowercase))
print(len(uppercase))

"""Python Program to Count Number of Lowercase Characters in a String"""

lowercase = re.findall(r'[a-z]',string1)
print(len(lowercase))

"""Python Program to Calculate the Number of Digits and Letters in a String"""

digits = re.findall(r'[0-9]',string1)
letters = re.findall(r'[a-zA-Z]',string1)
print("Digits:",len(digits))
print("letters:",len(letters))

"""Python Program to Calculate the Number of Words and the Number of Characters Present in a String"""
line = string1.split()
words = string1.split()
spaces = string1.split(" ")
charc = (len(line) - len(spaces))

print("Words",len(words))
print("Number of Characters",charc)

"""Python Program to Count the Number of Vowels in a String"""

vowels = re.findall(r'[aeiou]',string1)
print("Vowels",len(vowels))

"""Python Program to Calculate the Length of a String Without Using a Library Function"""

length = re.findall(r'[a-zA-Z]',string1)
print(len(length))


"""Python Program to Take in Two Strings and Display the Larger String without Using Built-in Functions"""

text1 = input()
text2 = input()

text1_str = re.findall(r'\S',text1)
text2_str = re.findall(r'\S',text2)

len_text1 = len(text1_str)
len_text2 = len(text2_str)

print(len_text1)
print(len_text2)

if len_text1 < len_text2:
    print(text2)
else:
    print(text1)