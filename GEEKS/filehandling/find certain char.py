"""I have a text file that contains:

motion
black
lotion
mansion
cardio
sensational

How would I use a regular expression to print all the words that contain 'ion'? So it prints:

motion
lotion
mansion
sensational"""
'''import re

with open("C:\\Users\\nekapoor\\git\\Python-and-Django\\PYTHON PROGRAMS\\file_data\\data.txt",'r',encoding='utf-8') as file1:

    matches = re.findall(r'.+ion.*?',string=file1)
    for word in matches:
        print(word)'''

import re
# file = open('filename').read()
file = open("C:\\Users\\nekapoor\\git\\Python-and-Django\\PYTHON PROGRAMS\\file_data\\data.txt").read()
matches = re.findall(r'.+oor.*?', string=file)
for word in matches:
    print(word)
