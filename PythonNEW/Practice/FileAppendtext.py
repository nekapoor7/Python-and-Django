"""Write a Python program to append text to a file and display the text."""

with open('C:\\Users\\nekapoor\\git\\Python-and-Django\\'
          'PYTHON PROGRAMS\\file_data\\data.txt','r',encoding='utf-8') as f:
    with open('C:\\Users\\nekapoor\\git\\Python-and-Django\\'
         'PYTHON PROGRAMS\\file_data\\data2.txt', 'a+',encoding='utf-8') as f1:
        line = f.read()
        message = input()
        f1.write(message + '\n\r')