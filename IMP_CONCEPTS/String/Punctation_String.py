#Program to count the total number of punctuation characters exists in a string.

string = str(input())
count = 0

for i in range(0,len(string)):
    if string[i] in ('!', "," ,"\'" ,";" ,"\"", ".", "-" ,"?"):
        count = count + 1

print(count)