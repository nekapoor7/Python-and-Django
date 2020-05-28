""" Write a Python function to check whether a number is in a given range."""

def test_range(n):
    s = int(input())
    e = int(input())
    if n in range(s,e):
        print( " %s is in the range"%str(n))
    else :
        print("The number is outside the given range.")
test_range(10)

