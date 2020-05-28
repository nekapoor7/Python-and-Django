"""Write a Python program to check a dictionary is empty or not."""

N = int(input())
d = {}
for i in range(N):
    key = input()
    value = input()
    d.update({key:value})

if len(d) > 1:
    print(d)
else:
    print("Dictionary is Empty")