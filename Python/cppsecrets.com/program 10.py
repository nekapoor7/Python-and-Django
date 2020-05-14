"""Python Program to Check if a String is a Palindrome or Not"""

text = input()

if text == text[::-1]:
    print("Palindrome")
else:
    print("Not Palindrome")