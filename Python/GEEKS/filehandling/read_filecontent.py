"""Python Program to Read the Contents of a File"""


with open("C:\\Users\\nekapoor\\git\\Python-and-Django\\PYTHON PROGRAMS\\file_data\\data.txt",'r',encoding='utf-8') as f:
    data = f.read()
    print(data)