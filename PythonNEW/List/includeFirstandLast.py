""" Write a Python program to generate and print a list of first and last 5 elements
where the values are square of numbers between 1 and 30 (both included). """

n1,n2 = list(map(int,input().split()))
l = []
for i in range(n1,n2 +1):
    i = i * i
    l.append(i)
ll = l[:5] +l[-5:]
print(ll)
