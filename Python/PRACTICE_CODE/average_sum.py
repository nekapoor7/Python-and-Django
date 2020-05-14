#Python Program to Calculate the Average of Numbers in a Given List

def average(list1):
    sum = 0
    avg = 0
    for i in list1:
        sum += i
        avg = sum / i
    print(avg)
    print(sum)

N = int(input())
list1 = list(map(int,input().split()))
average(list1)
