"""Write a Python program to append text to a file and display the text."""

with open("C:\\Users\\nekapoor\\git\\Python-and-Django\\PYTHON PROGRAMS\\file_data\\nehacopy.txt", 'r',
              encoding='utf-8') as f:
    with open("C:\\Users\\nekapoor\\git\\Python-and-Django\\PYTHON PROGRAMS\\file_data\\nehacopy.txt", 'a',
              encoding='utf-8') as f1:
        data = f.read()
        message = input()
        f1.write(message + '\n\r')