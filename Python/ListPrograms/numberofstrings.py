"""Write a Python program to count the number of strings where the string length is 2 or
more and the first and last character are same from a given list of strings. Go to the editor
Sample List : ['abc', 'xyz', 'aba', '1221']
Expected Result : 2"""

list1 = list(input().split())
print(list1)
count = 0

for char in list1:
    if len(char) > 2 and char[0] == char[-1]:
        count += 1
print(count)