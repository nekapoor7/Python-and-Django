#Python Program to Read the Contents of a File

f = open("C:\\Users\\nekapoor\\git\\Python-and-Django\\PYTHON PROGRAMS\\file_data\\data.txt",encoding='utf-8')
line = f.readline()

while(line != ""):
    print(line)
    line = f.readline()

f.close()