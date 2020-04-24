#Python Program to Read a String from the User and Append it into a File

string = str(input())
with open("C:\\Users\\nekapoor\\git\\Python-and-Django\\PYTHON PROGRAMS\\file_data\\word.txt",'a',encoding='utf-8') as file1:
    file1.write("\n")
    file1.write(string)

with open("C:\\Users\\nekapoor\\git\\Python-and-Django\\PYTHON PROGRAMS\\file_data\\word.txt",'r',encoding='utf-8') as fname:
    line = fname.readline()
    while line != "":
        print(line)
        line = fname.readline()





