"""Python Program to Find the Largest Number in a List"""

list1 = list(map(int,input().split()))

Var = max(x for x in list1 if x == max(list1))
print(Var)

"""Python Program to Find the Second Largest Number in a List"""

Sec_Var = max(x for x in list1 if x != max(list1))
print(Sec_Var)

"""Python Program to Find the Smallest Number in a List"""

Min_Var = min(x for x in list1 if x == min(list1))
print(Min_Var)

"""Python Program to Find the Second smallest Number in a List"""

Sec_Min_var = min(x for x in list1 if x != min(list1))
print(Sec_Min_var)