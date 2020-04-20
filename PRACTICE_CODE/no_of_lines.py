#Python Program to Count the Number of Words in a Text File
num_lines = 0
with open("C:\\Users\\nekapoor\\Python\\file_data\\data.txt",'r',encoding='utf-8') as filename:

    for line in filename:
        num_lines += 1
print("Number of lines:")
print(num_lines)
filename.close()