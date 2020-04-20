import math

while True:
    print(math.gcd(int(input()),int(input())))

'''def gcd(x,y):
    if y == 0:
        return x
    else:
        return gcd(y, x % y)

x, y = list(map(int,input().split()))
print(gcd(x,y))'''