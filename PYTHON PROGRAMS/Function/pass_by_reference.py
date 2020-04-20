# Driver Code (Note that lst is modified
# after function call

def myFunc(x):
    x[0] = "Neha"

list1 = [1,2,3,4,5]
myFunc(list1)
print(list1)