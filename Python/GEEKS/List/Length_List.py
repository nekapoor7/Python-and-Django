"""Python | Ways to find length of list"""

count = 0

list1 = list(map(int,input().split()))

for i in list1:
    count += 1
print(count)