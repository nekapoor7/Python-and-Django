#Python Program to Take in the Marks of 5 Subjects and Display the Grade

marks = list(map(int, input("Enter the  numbers in a Given List").split()))
print(marks)
sum = 0
avg = 0

for i in marks:
    sum += i
    avg = sum/i

if sum > 95:
    print("A+ Grade")
elif sum > 85:
    print("B+ Grade")
elif sum > 75:
    print("C Grade")
elif sum > 65:
    print("D Grade")
else:
    print("E Grade")