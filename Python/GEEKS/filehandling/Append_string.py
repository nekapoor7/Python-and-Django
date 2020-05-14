"""Python Program to Read a String from the User and Append it into a File"""

with open("C:\\Users\\nekapoor\\git\\Python-and-Django\\PYTHON PROGRAMS\\file_data\\data3.txt",'r',encoding='utf-8') as f:
    with open("C:\\Users\\nekapoor\\git\\Python-and-Django\\PYTHON PROGRAMS\\file_data\\data3.txt", 'a',
              encoding='utf-8') as f1:
        string1 = input()
        data = f.read()
        data = '\n'
        f1.write(string1)