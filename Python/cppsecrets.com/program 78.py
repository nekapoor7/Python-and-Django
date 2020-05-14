"""Python Program to Count the Number of Blank Spaces in a Text File"""

with open("C:\\Users\\nekapoor\\git\\Python-and-Django\\PYTHON PROGRAMS\\file_data\\word.txt",'r',encoding='utf-8') as file1:
    data = file1.read()
    line = data.splitlines()
    words = data.split()
    spaces = data.split(" ")
    charc = (len(data) - len(spaces))

    print(len(spaces))


