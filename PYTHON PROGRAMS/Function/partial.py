from functools import partial

def f(a,b,c,x):
    return 1000 * a + 100 * b + 10 * c + x

g = partial(f,1,2,3)

print(g(5))