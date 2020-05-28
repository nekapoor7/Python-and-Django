"""Ways to remove i’th character from string in Python"""

s = input()
i = int(input())
ss = s[:i] + s[i+1:]
print(ss)