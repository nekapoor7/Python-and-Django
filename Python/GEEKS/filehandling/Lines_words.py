"""Python Program to Count the Number of Words,lines,spaces,char in a Text File"""

with open("C:\\Users\\nekapoor\\git\\Python-and-Django\\PYTHON PROGRAMS\\file_data\\data.txt",'r',encoding='utf-8') as f:
    data = f.read()
    lines = data.splitlines()
    words = data.split()
    spaces = data.split(" ")
    charc = (len(data) - len(spaces))

    print(len(lines))
    print(len(words))
    print(len(spaces))
    print(charc)

"""Python Program that Reads a Text File and Counts the Number of Times a Certain Letter Appears in the Text File"""

print(open("C:\\Users\\nekapoor\\git\\Python-and-Django\\PYTHON PROGRAMS\\file_data\\data.txt").read().count(input()))