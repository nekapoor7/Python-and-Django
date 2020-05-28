"""Python program to check if a string is palindrome or not"""

s = input()
if s == s[::-1]:
    print("String is Palindome")
else:
    print("String is not Palindrome")