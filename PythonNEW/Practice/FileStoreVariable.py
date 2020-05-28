"""Write a Python program to read a file line by line store it into a variable."""

with open('C:\\Users\\nekapoor\\git\\Python-and-Django\\'
         'PYTHON PROGRAMS\\file_data\\data.txt', 'r',encoding='utf-8') as f:
        ff = f.readlines()
        print(ff)
