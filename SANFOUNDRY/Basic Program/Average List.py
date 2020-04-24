"""Python Program to Calculate the Average of Numbers in a Given List"""

N = int(input())
list1 = list(map(int,input().split()))
sum = 0
avg = 0.0

for i in list1:
    sum += i
    avg = sum / N

print(sum)
print(avg)



