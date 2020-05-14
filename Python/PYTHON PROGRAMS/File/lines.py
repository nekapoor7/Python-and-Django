#Python Program to Count the Number of Lines in a Text File

num_of_lines = 0
with open("C:\\Users\\nekapoor\\git\\Python-and-Django\\PYTHON PROGRAMS\\file_data\\data4.txt", 'r', encoding='utf-8') as f:
    for line in f:
        num_of_lines += 1

print("Number of lines",num_of_lines)

f.close()