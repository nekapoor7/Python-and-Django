#Program to determine whether two strings are the anagram

str1 = str(input())
str2 = str(input())

if len(str1) != len(str2):
    print("Both the strings are not anagram")
else:
    """Convert string into lower"""
    str1 = str1.lower()
    str2 = str2.lower()

    """ Sorted the strings"""
    str1 = ''.join(sorted(str1))
    str2 = ''.join(sorted(str2))

    """ Compare if both strings contains same number of characters then its ANAGRAM else not"""
    if str1 == str2:
        print("Anagram")
    else:
        print("Not Anagram")