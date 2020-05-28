"""String slicing in Python to rotate a string"""

def rotatestr(s,x):
    return s[-x:] + s[:-x]

print(rotatestr(input(),int(input())))