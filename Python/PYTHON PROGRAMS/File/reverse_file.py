#Python Program to Read the Contents of a File in Reverse Order

with open("C:\\Users\\nekapoor\\Python\\file_data\\data.txt", 'r', encoding='utf-8') as filename:
    with open("C:\\Users\\nekapoor\\Python\\file_data\\data2.txt", 'w', encoding='utf-8') as filename1:
        data = filename.read()
        file_1 = data[::-1]
        filename1.write(file_1)
        filename1.close()
