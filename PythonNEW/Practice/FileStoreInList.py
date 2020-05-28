"""Write a Python program to read a file line by line and store it into a list."""

with open('C:\\Users\\nekapoor\\git\\Python-and-Django\\'
         'PYTHON PROGRAMS\\file_data\\data.txt', 'r',encoding='utf-8') as f:
    l = []
    for line in f:
        l.append(line)
    print(l)