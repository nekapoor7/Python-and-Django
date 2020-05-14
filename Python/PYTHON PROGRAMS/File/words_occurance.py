#Python Program to Count the Occurrences of a Word in a Text File

string1 = str(input("Enter the string for which we need to count occurance"))
with open("C:\\Users\\nekapoor\\Python\\file_data\\data.txt", 'r', encoding='utf-8') as filename:
    k = 0

    for line in filename:
        words = line.split()
        for i in words:
            if (i == string1):
                k = k + 1

print(k)
