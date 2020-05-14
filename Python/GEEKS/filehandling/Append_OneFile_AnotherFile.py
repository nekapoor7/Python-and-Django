"""Python Program to Append the Contents of One File to Another File"""

with open("C:\\Users\\nekapoor\\git\\Python-and-Django\\PYTHON PROGRAMS\\file_data\\data1.txt",'r',encoding='utf-8') as f:
    with open("C:\\Users\\nekapoor\\git\\Python-and-Django\\PYTHON PROGRAMS\\file_data\\word.txt", 'a',
              encoding='utf-8') as f1:
        data = f.read()
        f1.write(data)