"""Write a Python program to read a file line by line store it into an array."""

with open("C:\\Users\\nekapoor\\git\\Python-and-Django\\PYTHON PROGRAMS\\file_data\\nehacopy.txt", 'r',
              encoding='utf-8') as f:
    l = []
    for line in f:
        l.append(line)
    print(l)