#Python Program to Append the Contents of One File to Another File

with open("C:\\Users\\nekapoor\\Python\\file_data\\data.txt", 'r', encoding='utf-8') as filename:
    with open("C:\\Users\\nekapoor\\Python\\file_data\\data3.txt", 'a', encoding='utf-8') as filename1:
        file_copy = filename.read()
        filename.close()

        filename1.write(file_copy)
        filename1.close()