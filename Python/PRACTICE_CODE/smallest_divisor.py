#Python Program to Find the Smallest Divisor of an Integer

N = int(input())
list1 = []

for i in range(2, N+1):
    if N % i == 0:
        list1.append(i)

list1.sort()
print(list1[0])