""". Write a Python program to flatten a given nested list structure. Go to the editor
Original list: [0, 10, [20, 30], 40, 50, [60, 70, 80], [90, 100, 110, 120]]
Flatten list:
[0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120]"""

def flatten(l):
    for i in l:
        if isinstance(i,(list,tuple)):
            for j in flatten(i):
                yield j
        else:
            yield i

l = [0, 10, [20, 30], 40, 50, [60, 70, 80], [90, 100, 110, 120]]
print(list(flatten(l)))

