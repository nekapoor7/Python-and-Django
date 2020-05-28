"""Write a Python function to find the Max of three numbers."""

def threenumbers(a,b,c):
    if a < b and b > c:
        return b
    elif b < c and c > a:
        return c
    else:
        return a

a,b,c = list(map(int,input().split()))
print(threenumbers(a,b,c))