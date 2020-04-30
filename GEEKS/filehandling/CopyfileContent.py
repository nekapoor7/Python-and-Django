"""Python Program to Copy the Contents of One File into Another"""

with open("C:\\Users\\nekapoor\\git\\Python-and-Django\\PYTHON PROGRAMS\\file_data\\data.txt",'r',encoding='utf-8') as f:
    with open("C:\\Users\\nekapoor\\git\\Python-and-Django\\PYTHON PROGRAMS\\file_data\\neha1_copy.txt", 'w',
              encoding='utf-8') as f1:
        data = f.read()
        f1.write(data)