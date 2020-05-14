"""Python Program that Displays which Letters are in the First String but not in the Second"""

list1 = list(map(str,input().split()))
list2 = list(map(str,input().split()))

setA = set(list1)
setB = set(list2)

diff = setA.difference(setB)

print(diff)

text1 = input()
text2 = input()

setC = set(text1)
setD = set(text2)

diff1 = setC.difference(setD)
Lp = ''.join(diff1)

print(Lp)

