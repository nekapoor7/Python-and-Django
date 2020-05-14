def highestNumber(l):
    myMax = l[0]
    for num in l:
        if myMax < num:
            myMax = num
    return myMax

list1 = list(map(int,input().split()))
print (highestNumber(list1))