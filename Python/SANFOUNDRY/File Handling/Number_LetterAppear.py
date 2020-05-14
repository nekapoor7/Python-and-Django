#Python Program that Reads a Text File and Counts the Number of Times a Certain Letter Appears in the Text File

word = input()
k= 0
with open("C:\\Users\\nekapoor\\git\\Python-and-Django\\PYTHON PROGRAMS\\file_data\\word.txt",'r',encoding='utf-8') as file1:
    for line in file1:
        words = line.split()
        for i in words:
            for letter in i:
                if letter == word:
                    k = k + 1
    print("Occurrences of the letter:")
    print(k)