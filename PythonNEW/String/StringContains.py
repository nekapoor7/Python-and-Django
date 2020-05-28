"""Write a Python function to convert a given string to all uppercase if it contains at least 2 uppercase
characters in the first 4 characters."""

def uppercase(s):
    if s[:4].contains(s.lower):
        ns = s.upper()
        return ns

s = input()
print(uppercase(s))