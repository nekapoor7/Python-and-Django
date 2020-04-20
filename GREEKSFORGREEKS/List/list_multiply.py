# Python3 program to multiply all values in the
# list using lambda function and reduce()

from functools import reduce

list1 = list(map(int,input().split()))

result = reduce((lambda x , y : x * y ),list1)
add = reduce((lambda x ,y : x + y),list1)

print(result)
print(add)
