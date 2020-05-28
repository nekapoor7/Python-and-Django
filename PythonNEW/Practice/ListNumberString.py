"""Write a Python program to count the number of strings where the string length is 2 or
 more and the first and last character are same from a given list of strings. Go to the editor
Sample List : ['abc', 'xyz', 'aba', '1221']
Expected Result : 2"""

l = list(input().split())
count = 0
for i in l:
    if i[0] == i[-1] and len(i) > 2:
        count += 1
print(count)