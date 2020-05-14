#The sort function can be used to sort the list in both ascending and descending order.

l = list(map(int,input().split()))

l[len(l)//2:]=l[len(l)//2:][::-1]

print(l)

