"""Python Program to Read a Text File and Print all the Numbers Present in the Text File"""
import re

with open("C:\\Users\\nekapoor\\git\\Python-and-Django\\PYTHON PROGRAMS\\file_data\\data.txt",'r',encoding='utf-8') as file1:
    data = file1.read()
    print(data)

    numpre = re.findall(r'[0-9]',data)
    print(len(numpre))