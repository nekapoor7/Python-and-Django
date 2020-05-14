# After below line link of x with previous
# object gets broken. A new object is assigned
# to x.

def myFunc(x):
    x = [10,20,30]

list1 = [10,20,30,40,50]
myFunc(list1)
print(list1)