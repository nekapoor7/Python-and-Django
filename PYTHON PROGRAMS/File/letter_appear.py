#Python Program that Reads a Text File and Counts the Number of Times a Certain Letter Appears in the Text File

string1 = str(input("Enter the letter"))
with open("C:\\Users\\nekapoor\\Python\\file_data\\data.txt", 'r', encoding='utf-8') as filename:
    k = 0
    for line in filename:
            words = line.split()
            for i in words:
                for letter in i:
                    if(letter == string1):
                        k = k + 1
print(k)