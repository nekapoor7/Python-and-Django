"""Python Program to Read the Contents of a File

Python Program to Count the Number of Words in a Text File

Python Program to Count the Number of Lines in a Text File"""


""" Differnce between read(),readline(),readlines() and xreadlines()"""

'''1. read() ->  reads an entire file and returns it
    2. readline() -> reads a single line from file with the new line at the end
    3. readlines() -> returns a list containing all the lines in the file
    4. xreadlines() -> Returns a generator to loop over every single line in the file '''

with open("C:\\Users\\nekapoor\\git\\Python-and-Django\\PYTHON PROGRAMS\\file_data\\data.txt",'r',encoding='utf-8') as file1:
    data = file1.read()
    print(data)

num_line = 0
with open("C:\\Users\\nekapoor\\git\\Python-and-Django\\PYTHON PROGRAMS\\file_data\\data.txt",'r',encoding='utf-8') as file1:
    for line in file1:
        num_line += 1
    print(num_line)

num_words = 0
with open("C:\\Users\\nekapoor\\git\\Python-and-Django\\PYTHON PROGRAMS\\file_data\\data.txt",'r',encoding='utf-8') as file1:
    for line in file1:
        words = line.split()
        num_words += len(words)
    print(num_words)

num_char = 0
with open("C:\\Users\\nekapoor\\git\\Python-and-Django\\PYTHON PROGRAMS\\file_data\\data.txt",'r',encoding='utf-8') as file1:
    for line in file1:
        for char in line:
            num_char += 1
    print(num_char)