"""Python program to concatenate strings in a string collection."""

str1 = list(map(str,input().split()))

value = ''

for var in str1:
    value += var

print(value)