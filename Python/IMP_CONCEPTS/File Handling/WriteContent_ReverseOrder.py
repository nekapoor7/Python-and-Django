"""" Python Program to read content from one file and reverse the content to another file while writing"""

with open("C:\\Users\\nekapoor\\git\\Python-and-Django\\PYTHON PROGRAMS\\file_data\\data.txt", 'r', encoding='utf-8') as file1:
    with open("C:\\Users\\nekapoor\\git\\Python-and-Django\\PYTHON PROGRAMS\\file_data\\data_copy.txt", 'w',
              encoding='utf-8') as file2:
        data = file1.read()
        reverse_content = data[::-1]
        file2.write(reverse_content)
        