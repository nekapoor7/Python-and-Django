"""Write a Python program to get a string made of the first 2 and the last 2 chars from a given a string.
If the string length is less than 2, return instead of the empty string. Go to the editor
Sample String : 'w3resource'
Expected Result : 'w3ce'
Sample String : 'w3'
Expected Result : 'w3w3'
Sample String : ' w'
Expected Result : Empty String
Click me to see the sample solution"""

t1,t2 = list(input().split())
newstring = t1[:2] + t1[-2:]
print(newstring)

if len(t2) < 2:
    print("Empty String")
else:
    print(t2*2)