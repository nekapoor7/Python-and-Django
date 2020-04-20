#Python Program to Count the Number of Words in a Text File

num_of_words = 0
with open("C:\\Users\\nekapoor\\Python\\file_data\\data.txt", 'r', encoding='utf-8') as f:

    for line in f:
        words = line.split()
        num_of_words += len(words)

print("Number of words",num_of_words)

f.close()

