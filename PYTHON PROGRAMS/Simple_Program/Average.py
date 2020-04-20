#Python Program to Calculate the Average of Numbers in a Given List


list1 = list(map(int, input("Enter the  numbers in a Given List").split()))
sum = 0
avg = 0.0

for i in list1:
    sum += i
    avg = sum/i

print(list1)
print(sum)
print(avg)