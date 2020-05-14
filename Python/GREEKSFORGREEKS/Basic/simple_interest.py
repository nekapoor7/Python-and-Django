#Python Program for simple interest

def simple(p,r,t):
    SI = (p*r*t)/100;
    return SI

p = int(input())
r = int(input())
t = int(input())
print(simple(p,r,t))