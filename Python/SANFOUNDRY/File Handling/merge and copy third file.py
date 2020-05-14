""" Merge Content of one file to another file and copy to third file"""

"""Inline Function """

""" Creating a list of filenames"""

data1 = data2 = " "

with open("C:\\Users\\nekapoor\\git\\Python-and-Django\\PYTHON PROGRAMS\\file_data\\data4.txt",'r',encoding='utf-8') as file1:
    data1 = file1.read()

with open("C:\\Users\\nekapoor\\git\\Python-and-Django\\PYTHON PROGRAMS\\file_data\\data.txt",'r',encoding='utf-8') as file2:
    data2 = file2.read()

    # Merging 2 files
    # To add the data of file2
    # from next line
    data1 += "\n"
    data1 += data2

with open("C:\\Users\\nekapoor\\git\\Python-and-Django\\PYTHON PROGRAMS\\file_data\\merge_file.txt",'w',encoding='utf-8') as file3:
    file3.write(data1)


