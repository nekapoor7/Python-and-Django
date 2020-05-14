'''

Rotate the list by right by the given integer
input1 : [1,2,3,4,5], 2 -> [4,5,1,2,3]
input2 : [1,2,3,0,3], 2 -> [0,3,1,2,3]

'''

l = [1,2,3,4,5]

def rorate(l,x):
    ll = l[-x:] + l[:-x]
    return ll

l = [1,2,3,4,5]
N = int(input())
print(rorate(l,N))