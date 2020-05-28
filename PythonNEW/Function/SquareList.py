"""Write a Python function to create and print a list where the values are
 square of numbers between 1 and 30 (both included)."""

def square(s,e):
    l1 = []
    for i in range(s,e +1):
        i = i*i
        l1.append(i)
    return l1


s,e = list(map(int,input().split()))
print(square(s,e))