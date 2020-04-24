"""Python Program to read the content from File and convert it to a list"""

with open("C:\\Users\\nekapoor\\git\\Python-and-Django\\PYTHON PROGRAMS\\file_data\\word.txt", 'r', encoding='utf-8') as file1:
    linelist = file1.readlines()

    linelist = list()
    with open("C:\\Users\\nekapoor\\git\\Python-and-Django\\PYTHON PROGRAMS\\file_data\\word.txt", 'r',
              encoding='utf-8') as file1:
        for line in file1:
            linelist.append(line)

    linelist = [line.rstrip('\n').split() for line in open("C:\\Users\\nekapoor\\git\\Python-and-Django\\PYTHON PROGRAMS\\file_data\\word.txt")]
    print(linelist)

