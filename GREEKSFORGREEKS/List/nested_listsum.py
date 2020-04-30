#Iterate through a Nested List

L = [[1, 2, 3]]
'''sum = 0
for list in L:
    for number in list:
        print(number, end=' ')
        sum += number
print(sum)'''

result = sum(sum(x) if isinstance(x,list) else x for x in L)

print(result)

sum(sum(x) if isinstance(x,list) else x for x in L)
print(result)