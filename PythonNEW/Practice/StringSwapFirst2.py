"""Write a Python program to get a single string from two given strings,
separated by a space and swap the first two characters of each string. Go to the editor
Sample String : 'abc', 'xyz'
Expected Result : 'xyc abz'"""

s = input()
ss = s[-3:-1] + s[2] + ' ' + s[:2] + s[-1:]

print(ss)