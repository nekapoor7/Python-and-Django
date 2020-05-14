#Python Program to Read a String from the User and Append it into a File


with open("C:\\Users\\nekapoor\\Python\\file_data\\data.txt", 'a', encoding='utf-8') as f:
    string1 = str(input("Enter the string"))
    f.write("\n")
    f.write(string1)
    f.close()

print("Contents of appended file:");

with open("C:\\Users\\nekapoor\\Python\\file_data\\data.txt", 'r', encoding='utf-8') as f2:
    for line in f2:
        print(line,end='')
'''result = [line.split(',') for line in f2.readline()]
print(result)'''
f2.close()

with open("C:\\Users\\nekapoor\\Python\\file_data\\data.txt", 'r', encoding='utf-8') as f1:
    num_of_line = 0
    for line in f1:
        num_of_line += 1
print("Number of lines after append",num_of_line)
f1.close()

