"""Write a Python function to sum all the numbers in a list. Go to the editor
Sample List : (8, 2, 3, 0, 7)
Expected Output : 20 """

def sumlist(l):
    s = sum(map(int,l))
    return s

l = list(map(int,input().split()))
print(sumlist(l))