"""Python program to check if a string is palindrome or not"""

string1 = input()
if string1 == string1[::-1]:
    print("Palindrome")
else:
    print("Not Palindrome")