'''Task

The students of District College have subscriptions to English and French newspapers.
Some students have subscribed only to English, some have subscribed only to French, and some have subscribed to both newspapers.

You are given two sets of student roll numbers. One set has subscribed to the English newspaper, one set has subscribed
 to the French newspaper. Your task is to find the total number of students who have subscribed to both newspapers.'''

e = input()
el = set(map(int,input().split()))
f = input()
fl = set(map(int,input().split()))

i = el.intersection(fl)
#u = el.union(f1)
#d = el.difference(f1)
#i = el.symmetric_difference(fl)

#print(i)

print(len(i))

'''    n, set_A = int(input()), set(input().split())
    for _ in range(int(input())):
        op, set_B = input().split(), input().split()
        if op[0] == 'intersection_update':
            set_A.intersection_update(set_B)
        elif op[0] == 'difference_update':
            set_A.difference_update(set_B)
        elif op[0] == 'symmetric_difference_update':
            set_A.symmetric_difference_update(set_B)
        elif op[0] == 'update':
            set_A.update(set_B)
    print(sum(map(int, set_A)))'''