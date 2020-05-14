"""Python Program to Read a String from the User and Append it into a File"""


with open("C:\\Users\\nekapoor\\git\\Python-and-Django\\PYTHON PROGRAMS\\file_data\\data.txt",'r',encoding='utf-8') as f:
    with open("C:\\Users\\nekapoor\\git\\Python-and-Django\\PYTHON PROGRAMS\\file_data\\data.txt", 'a',
              encoding='utf-8') as f1:
        text = input()
        data = f.read()
        data = '\n'
        f1.write(text)
