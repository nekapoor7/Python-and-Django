"""Write a Python program to find missing and additional values in two lists."""

l = list(input().split())
ll = list(input().split())

missing_l = list(set(l).difference(set(ll)))
print(' '.join(missing_l))

missing_ll = list(set(ll).difference(set(l)))
print(' '.join(missing_ll))