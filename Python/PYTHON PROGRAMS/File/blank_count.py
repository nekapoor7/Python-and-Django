#Python Program to Count the Number of Blank Spaces in a Text File
k = 0
'''with open("C:\\Users\\nekapoor\\Python\\file_data\\word.txt", 'r', encoding='utf-8') as filename:
    for line in filename:
        words = line.split()
        for i in words:
            for letter in i:
                if(letter.isspace):
                    k=k+1

print(k)'''
with open("C:\\Users\\nekapoor\\Python\\file_data\\word.txt", 'r', encoding='utf-8') as filename:
    for line in filename:
            words = line.split()
            for i in words:
                for letter in i:
                    if(letter.isspace):
                        k=k+1
print("Occurrences of blank spaces:")
print(k)

filename.close()