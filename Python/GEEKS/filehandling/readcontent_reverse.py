"""Python Program to Read the Contents of a File in Reverse Order"""

with open("C:\\Users\\nekapoor\\git\\Python-and-Django\\PYTHON PROGRAMS\\file_data\\data1.txt",'r',encoding='utf-8') as f:
    data = f.read()
    reverse_content = data[::-1]
    print(reverse_content)
