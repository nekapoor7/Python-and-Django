#Python Program to Find the Second Largest Number in a List

'''list1 = list(map(int, input("Enter the  numbers in a Given List").split()))

second_max = max([num for num in list1 if num != max(list1)])

print(second_max)'''

list1 = list(map(int, input("Enter the  numbers in a Given List").split()))

max = max(list1[0],list1[1])
secondmax = min(list1[0],list1[1])

for i in range(2,len(list1)):
    if list1[i] > max:
        secondmax = max
        max = list1[i]
    else:
        if list1[i] > secondmax:
            secondmax = list1[i]

print("The second highest number in the list",str(secondmax))
