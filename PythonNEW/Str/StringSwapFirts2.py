"""Write a Python program to get a single string from two given strings,
 separated by a space and swap the first two characters of each string. Go to the editor
Sample String : 'abc', 'xyz'
Expected Result : 'xyc abz'"""

def swap2char(a,b):
    return b[:2]+a[2:] + ' ' + a[:2] + b[2:]

print(swap2char('abc','xyz'))