"""Write a Python program to extend a list without append. Go to the editor
Sample data: [10, 20, 30]
[40, 50, 60]
Expected output : [40, 50, 60, 10, 20, 30]"""

l1 = list(map(int,input().split()))
l2 = list(map(int,input().split()))
l1[:0] = l2
print(l1)