l = [[1,4,3], [2,2,4], [3,1,5]]

s = sum(sum(x) if isinstance(x,list) else x for x in l)

print(s)