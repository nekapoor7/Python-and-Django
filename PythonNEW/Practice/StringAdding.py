"""Write a Python program to add 'ing' at the end of a given string (length should be at least 3).
 If the given string already ends with 'ing' then add 'ly' instead. If the string length of the given string
  is less than 3, leave it unchanged. Go to the editor
Sample String : 'abc'
Expected Result : 'abcing'
Sample String : 'string'
Expected Result : 'stringly'"""

s = input()
s1 = 'ing'
s2 = 'ly'
if s[-3:] == s1:
    ns = s + s2
    print(ns)
elif len(s) >= 3:
    ns = s + s1
    print(ns)
else:
    print(s)