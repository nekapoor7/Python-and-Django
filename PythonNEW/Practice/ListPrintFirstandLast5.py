"""Write a Python program to generate and print a list of first and last 5 elements where the values are square of numbers
 between 1 and 30 (both included)."""

""" Write a Python program to generate and print a list except for the first 5 elements, 
where the values are square of numbers between 1 and 30 (both included). """

s,e = list(map(int,input().split()))
l = []

for i in range(s,e+1):
    i = i * i
    l.append(i)
print(l[:5]+l[-5:])
print(l[5:])


