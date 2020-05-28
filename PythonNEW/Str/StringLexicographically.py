"""Write a Python program to sort a string lexicographically."""

s = input().split()
for word in sorted(s,key=str.lower):
    print(word,end=' ')
