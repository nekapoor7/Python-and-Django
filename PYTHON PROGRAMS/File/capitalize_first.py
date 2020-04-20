#Python Program to Read a File and Capitalize the First Letter of Every Word in the File

with open("C:\\Users\\nekapoor\\Python\\file_data\\data.txt", 'r', encoding='utf-8') as filename:
    for line in filename:
        word = line.title()
        capital = line.upper()
        lower = line.lower()
        print(word)

