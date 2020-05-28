"""Write a Python program to capitalize first and last letters of each word of a given string"""

s = 'ravi had been saying that he had been there'
ss = [word[0:1].upper()+word[1:-1].lower()+word[-1:].upper() for word in s.split()]
print(" ".join(ss))