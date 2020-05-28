"""Write a Python program to read last n lines of a file."""

with open('C:\\Users\\nekapoor\\git\\Python-and-Django\\'
         'PYTHON PROGRAMS\\file_data\\data.txt', 'r',encoding='utf-8') as f:
    N = int(input())
    for line in f.readlines()[-N:]:
        print(line,end=' ')
