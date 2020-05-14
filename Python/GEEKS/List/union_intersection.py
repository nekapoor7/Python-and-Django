"""Python Program to Find the Union of two Lists"""

list2 = input()
list3 = input()

'''setA = set(list2)
setB = set(list3)

Union_list = setA.union(setB)
Intersection_list = setA.intersection(setB)

list4 = list(Union_list)
list5 = list(Intersection_list)

print(list4)
print(list5)'''

union = list(set().union(list2,list3))
print(union)

intersection = list(set().intersection(list2,list3))
print(intersection)

