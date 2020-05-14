#Python Program to Read a Text File and Print all the Numbers Present in the Text File

with open("C:\\Users\\nekapoor\\Python\\file_data\\data.txt", 'r', encoding='utf-8') as filename:
    for line in filename:
        words = line.split()
        for i in words:
            for letter in i:
                if (letter.isdigit()):
                    print(letter)