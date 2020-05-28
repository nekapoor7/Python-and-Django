"""Write a Python function that takes two lists and returns True if they have at least one common member."""

def common(l,l1):
    result = False
    for x in l:
        for y in l1:
            if x == y:
               result = True
    return result

l = list(input().split())
l1 = list(input().split())
print(common(l,l1))