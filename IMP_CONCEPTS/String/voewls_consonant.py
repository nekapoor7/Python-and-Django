#Program to count the total number of vowels and consonants in a string.

vcount = 0
ccount = 0
str = str(input())

str = str.lower()
for i in range(0,len(str)):
    if str[i] in ('a',"e","i","o","u"):
        vcount = vcount + 1
    elif str[i] >= 'a' and str[i] <= 'z':
        ccount = ccount + 1

print(vcount)
print(ccount)