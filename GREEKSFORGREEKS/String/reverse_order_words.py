#Reverse words in a given String in Python

string1 = input()
string2 = string1.split(' ')
string3 = string2[::-1]

for i in string3:
    print(i,end=" ")