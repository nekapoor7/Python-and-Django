"""Python Program that Reads a Text File and Counts the Number of Times a Certain Letter Appears in the Text File"""
import re
with open("C:\\Users\\nekapoor\\git\\Python-and-Django\\PYTHON PROGRAMS\\file_data\\data.txt",'r',encoding='utf-8') as file1:
    data = file1.read()
    print(data)

    text = input()
    letter_count = re.search(r'[A-Za-z]',data)
    print(len(letter_count))