"""Python Program to find Student Grade"""

list1 = list(map(int,input().split()))
avg = 0.0
sum = 0

for i in list1:
    sum += i
    avg = sum / len(list1)

print(sum)
print(avg)

if avg > 90:
    print("A+ Grade")
elif avg >= 80 and avg <= 90:
    print("B Grade")
elif avg >= 70 and avg <= 80:
    print("C Grade")
else:
    print("D Grade")