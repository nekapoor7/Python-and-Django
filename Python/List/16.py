""" Write a Python program to generate and print a list of first and last 5 elements
where the values are square of numbers between 1 and 30 (both included)."""

n1,n2 = list(map(int,input().split()))
l = []
l2 = []
for i in range(n1,n2+1):
    l.append(i*i)
print(l)
l2 = l[0:5]+l[-5:]
print(l2)

""" Write a Python program to generate and print a list except for the first 5 elements, 
where the values are square of numbers between 1 and 30 (both included)."""
l3 = l[5:]
print(l3)