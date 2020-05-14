"""Python Program to get prime numbers between intervals"""
import random
lower,upper = list(map(int,input().split()))

primenum = [x for x in range(lower,upper) if(all(x % j for j in range(2, x)))]

print(primenum)