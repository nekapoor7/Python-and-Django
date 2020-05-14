#Find words which are greater than given length k

#Find words which are greater than given length k

str = input()
value_k = int(input())
string = []

text = str.split(" ")

for char in text:
    if len(char) > value_k:
        string.append(char)
print(string)