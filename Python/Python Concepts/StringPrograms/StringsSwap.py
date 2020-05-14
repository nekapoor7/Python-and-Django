"""Write a Python program to get a single string from two given strings,
separated by a space and swap the first two characters of each string. Go to the editor
Sample String : 'abc', 'xyz'
Expected Result : 'xyc abz'"""

s1,s2 = list(input().split())
t1 = s2[:2] + s1[2:]
t2 = s1[:2] + s2[2:]
print(t1,t2)