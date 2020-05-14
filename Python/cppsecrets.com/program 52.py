"""Python Program to Put Even and Odd elements in a List into Two Different Lists"""

list1 = list(map(int,input().split()))

evenlist = list(filter(lambda varx : varx % 2 == 0,list1))

oddlist = list(filter(lambda varx : varx % 2 != 0,list1))

print(evenlist)
print(oddlist)