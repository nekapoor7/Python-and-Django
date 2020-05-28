"""Write a Python program to count number of substrings with same first and last characters of a given string."""

def substringFirstLast(s):
    result = 0
    n = len(s)
    for i in range(n):
        for j in range(i,n):
            if s[i] == s[j]:
                result = result + 1
    return result

print(substringFirstLast(input()))