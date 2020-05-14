"""Write a Python program to read an entire text file."""

with open("C:\\Users\\nekapoor\\git\\Python-and-Django\\PYTHON PROGRAMS\\file_data\\data.txt",'r',encoding='utf-8') as f:
    data = f.read()
    print(data)