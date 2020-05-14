"""Python Program to Generate a Dictionary that Contains Numbers (between 1 and n) in the Form (x,x*x)."""

num = int(input())
d = {x : x*x for x in range(1,num+1)}

print(d)
