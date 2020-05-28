"""Python | Check if a given string is binary string or not"""

s = input()
if all(c in '01' for c in s):
    print("True")
else:
    print("False")
