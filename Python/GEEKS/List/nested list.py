"""Nested list sort python 3"""


l = [[1,4,3], [2,2,4], [3,1,5]]

sl = sorted(l,key=lambda x:x[1])

print(sl)

s = sum(sum(x) if isinstance(x,list) else x for x in l)

print(s)