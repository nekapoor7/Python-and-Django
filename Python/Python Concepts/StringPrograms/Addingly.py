"""Write a Python program to add 'ing' at the end of a given string (length should be at least 3).
If the given string already ends with 'ing' then add 'ly' instead. If the string length of the given string is less than 3,
leave it unchanged. Go to the editor
Sample String : 'abc'
Expected Result : 'abcing'
Sample String : 'string'
Expected Result : 'stringly'"""

text = input()
s1 = 'ing'
s2 = 'ly'

if s1 in text:
    string = text + s2
    print(string)
elif len(text) >= 3:
    new_string = text + s1
    print(new_string)
else:
    print(text)

