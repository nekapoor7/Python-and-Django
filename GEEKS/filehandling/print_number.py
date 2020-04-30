"""Python Program to Read a Text File and Print all the Numbers Present in the Text File"""
import re

with open("C:\\Users\\nekapoor\\git\\Python-and-Django\\PYTHON PROGRAMS\\file_data\\data1.txt",'r',encoding='utf-8') as f:
    data = f.read()
    number = re.findall(r'[0-9]+',data)
    print(number)
    print(type(number))
    value = ' '.join(number)
    print(value)
    print(type(value))
