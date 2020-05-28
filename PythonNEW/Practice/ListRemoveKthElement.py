"""Write a Python program to remove the K'th element from a given list, print the new list. Go to the editor
Original list:
[1, 1, 2, 3, 4, 4, 5, 1]
After removing an element at the kth position of the said list:
[1, 1, 3, 4, 4, 5, 1]"""

l = list(input().split())
k = int(input())

ll = l[:k] + l[k+ 1:]
print(' '.join(ll))