"""Python program to find uncommon words from two Strings"""

s = input().split()
s1 = input().split()
uncommon = str(set(s).difference(set(s1)))
print(uncommon)