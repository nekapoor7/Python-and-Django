"""Python Program to Take in the Marks of 5 Subjects and Display the Grade"""

def Grade(list1):
    sum , avg = 0 , 0
    for i in list1:
        sum += i
        avg = sum / N
    print(avg)
    if avg > 90:
        return "A+ Grade"
    elif avg > 80 and avg <=90:
        return "B+ Grade"
    elif avg > 70 and avg <= 80:
        return "C Grade"
    else:
        return "D Grade"

N = int(input())
list1 = list(map(int,input().split()))
print(Grade(list1))