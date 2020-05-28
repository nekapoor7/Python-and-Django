"""Write a Python function that checks whether a passed string is palindrome or not. Go to the editor
Note: A palindrome is a word, phrase, or sequence that reads the same backward as forward, e.g., madam or nurses run."""

def Palindrome(s):
    if s == s[::-1]:
        return "String Palindrome"
    else:
        return "String is not Palindrome"

s = input()
print(Palindrome(s))