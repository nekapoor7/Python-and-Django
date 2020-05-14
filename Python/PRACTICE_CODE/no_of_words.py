#Python Program to Count the Number of Words in a Text File

with open("C:\\Users\\nekapoor\\Python\\file_data\\data.txt",'r',encoding='utf-8') as filename:
    no_of_words = 0

    for line in filename:
        words = line.split()
        no_of_words += len(words)

print(no_of_words)

filename.close()
