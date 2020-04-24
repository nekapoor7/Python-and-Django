#Program to find all possible subsets of a string.

string = str(input())
n = len(string)
list1 = []

for i in range(0,n):
    for j in range(i,n):
        list1.append(string[i:j+1])

for i in list1:
    print(i)