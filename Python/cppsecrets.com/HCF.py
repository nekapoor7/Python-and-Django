"""Python program to find H.C.F"""
import math

a , b = list(map(int,input().split()))

hcf = math.gcd(a,b)

print(hcf)