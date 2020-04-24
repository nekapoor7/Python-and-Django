#Python | Multiply all numbers in the list

from functools import reduce

list1 = list(map(int,input().split()))

result = reduce((lambda x , y : x * y),list1)
sum = reduce((lambda x , y : x + y),list1)
diff = reduce((lambda x , y: x - y),list1)

print(result)
print(sum)
print(diff)