#Python Program to Count the Number of Vowels in a String

string = input()
string = string.lower()
count = 0
count1 = 0

for i in range(0,len(string)):
    if string[i] in ("a","e","i","o","u"):
        count = count + 1
    elif string[i] >='a' and string[i] <= 'z':
        count1 = count1 + 1


print(count)
print(count1)