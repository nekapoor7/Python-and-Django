"""Python Program to Read the Contents of a File"""

with open("C:\\Users\\nekapoor\\git\\Python-and-Django\\PYTHON PROGRAMS\\file_data\\word.txt",'r',encoding='utf-8') as file1:
    data = file1.read()
    print(data)