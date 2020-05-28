"""Write a Python program to replace the last element in a list with another list. Go to the editor
Sample data : [1, 3, 5, 7, 9, 10], [2, 4, 6, 8]
Expected Output: [1, 3, 5, 7, 9, 2, 4, 6, 8]"""

l = [1, 3, 5, 7, 9, 10]
l1 = [2, 4, 6, 8]
l[-1:] = l1
print(l)