"""Python Program to Copy the Contents of One File into Another"""

with open("C:\\Users\\nekapoor\\git\\Python-and-Django\\PYTHON PROGRAMS\\file_data\\data.txt",'r',encoding='utf-8') as file1:
    with open("C:\\Users\\nekapoor\\git\\Python-and-Django\\PYTHON PROGRAMS\\file_data\\data_copy_copy.txt", 'w',
              encoding='utf-8') as file2:
        for line in file1:
            file2.write(line)
