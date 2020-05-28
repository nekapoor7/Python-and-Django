"""Write a Python function to reverses a string if it's length is a multiple of 4. """

def StringReverse(s):
    if len(s) % 4 == 0:
        return s[::-1]
    else:
        return s

print(StringReverse(input()))