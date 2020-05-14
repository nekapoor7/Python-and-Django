#Python program to find smallest number in a list

'''for i in list1:
    var = min(list1)
print(var)'''

def smallestNumber(l):
    myMin = l[0]
    for num in l:
        if myMin > num:
            myMin = num
    return myMin

list1 = list(map(int,input().split()))
print (smallestNumber(list1))
