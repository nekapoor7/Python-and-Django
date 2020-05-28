"""Write a Python program to convert a list of multiple integers into a single integer. Go to the editor
Sample list: [11, 33, 50]
Expected Output: 113350"""

l = list(map(int,input().split()))
print(l)
print("".join(map(str,l)))