
limit = int(input("Enter the limit"))
generator = (num ** 2 for num in range(limit))
for num in generator:
    str(num)

list1 = list(map(int,str(num)))

print(list1)
print(type(list1))