"""Write a Python program to split a given list into two parts where the length of the first part of the list is given.
 Go to the editor
Original list:
[1, 1, 2, 3, 4, 4, 5, 1]
Length of the first part of the list: 3
Splited the said list into two parts:
([1, 1, 2], [3, 4, 4, 5, 1])"""

l = list(input().split())
N = int(input())
ll = l[:N],l[N:]
print(ll)
