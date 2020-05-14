"""Write a Python program to write a list to a file"""
l = list(input().split())
with open("C:\\Users\\nekapoor\\git\\Python-and-Django\\PYTHON PROGRAMS\\file_data\\nehacopy.txt", 'w',
              encoding='utf-8') as f:
        for lines in l:
            f.write("%s\n" % lines)