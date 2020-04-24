#Program to determine whether two strings are the anagram

NO_OF_CHARS = 256

def string_anagram(str1,str2):

    count1 = [0] * NO_OF_CHARS
    count2 = [0] * NO_OF_CHARS

    for i in str1:
        count1[ord(i)] += 1

    for i in str2:
        count2[ord(i)] += 1


    if len(str1) != len(str2):
        return 0

    for i in range(NO_OF_CHARS):
        if count1[i] != count2[i]:
            return 0

    return 1

str1 = str(input())
str2 = str(input())
if string_anagram(str1,str2):
    print("String Anagram")
else:
    print("String are not Anagram")
