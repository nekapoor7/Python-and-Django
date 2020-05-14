# Python code to demonstrate
# checking of element existence
# using loops and in

list1 = list(map(int,input().split()))
num = int(input())
if num in list1:
    print("Element Found")
else:
    print("Element Not Found")


