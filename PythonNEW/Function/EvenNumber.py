"""Write a Python program to print the even numbers from a given list. Go to the editor
Sample List : [1, 2, 3, 4, 5, 6, 7, 8, 9]
Expected Result : [2, 4, 6, 8]"""

def EvenNumber(l):
    l1 = []
    for i in l:
        if i % 2 == 0:
            l1.append(i)
    return l1

l = list(map(int,input().split()))
print(EvenNumber(l))