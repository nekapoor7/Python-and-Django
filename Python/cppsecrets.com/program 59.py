"""Python Program to Sort a List According to the Length of the Elements"""

list_name = list(map(str,input().split()))

sortlist = sorted(list_name,key=len)

print(sortlist)