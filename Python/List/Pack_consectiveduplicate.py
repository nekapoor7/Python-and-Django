"""Write a Python program to pack consecutive duplicates of a given list elements into sublists. Go to the editor
Original list:
[0, 0, 1, 2, 3, 4, 4, 5, 6, 6, 6, 7, 8, 9, 4, 4]
After packing consecutive duplicates of the said list elements into sublists:
[[0, 0], [1], [2], [3], [4, 4], [5], [6, 6, 6], [7], [8], [9], [4, 4]]"""
from itertools import groupby
l = [0, 0, 1, 2, 3, 4, 4, 5, 6, 6, 6, 7, 8, 9, 4, 4]
l1 = [list(group) for key,group in groupby(l)]
print(l1)

"""Write a Python program to flatten a given nested list structure. Go to the editor
Original list: [0, 10, [20, 30], 40, 50, [60, 70, 80], [90, 100, 110, 120]]
Flatten list:
[0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120]"""
from itertools import chain
newlist =[[52, None, None], [129, None, None], [56, None, None], [111, None, None],
          [22, None, None], [33, None, None], [28, None, None], [52, None, None],
          [52, None, None], [52, None, None], [129, None, None], [56, None, None],
          [111, None, None], [22, None, None], [33, None, None], [28, None, None]]
newlist = list(chain(*newlist))
print(newlist)

l2 = [[1, 2, 3], [4, 5, 6], [7], [8, 9]]
l2 = list(chain(*l2))
print(l2)

l3 = [0, 10, [20, 30], 40, 50, [60, 70, 80], [90, 100, 110, 120]]
def flatten(container):
    for i in container:
        if isinstance(i, (list,tuple)):
            for j in flatten(i):
                yield j
        else:
            yield i

print(list(flatten(l3)))

"""Write a Python program to create a list reflecting the run-length encoding 
from a given list of integers or a given list of characters. Go to the editor
Original list:
[1, 1, 2, 3, 4, 4.3, 5, 1]
List reflecting the run-length encoding from the said list:
[[2, 1], [1, 2], [1, 3], [1, 4], [1, 4.3], [1, 5], [1, 1]]
Original String:
automatically
List reflecting the run-length encoding from the said string:
[[1, 'a'], [1, 'u'], [1, 't'], [1, 'o'], [1, 'm'], [1, 'a'], [1, 't'], [1, 'i'], [1, 'c'], [1, 'a'], [2, 'l'], [1, 'y']]"""
l4 = 'automatically'
l5 = [[len(list(group)),key] for key,group in groupby(l4)]

print(l5)

"""Write a Python program to create a list reflecting the modified run-length encoding
 from a given list of integers or a given list of characters. Go to the editor
Original list:
[1, 1, 2, 3, 4, 4, 5, 1]
List reflecting the modified run-length encoding from the said list:
[[2, 1], 2, 3, [2, 4], 5, 1]
Original String:
aabcddddadnss
List reflecting the modified run-length encoding from the said string:
[[2, 'a'], 'b', 'c', [4, 'd'], 'a', 'd', 'n', [2, 's']]"""

ll = [1, 1, 2, 3, 4, 4, 5, 1]
ll1 = [(list(group)) for key,group in groupby(ll)]
print(ll1)

"""Write a Python program to split a given list into two parts where the length
 of the first part of the list is given. Go to the editor
Original list:
[1, 1, 2, 3, 4, 4, 5, 1]
Length of the first part of the list: 3
Splited the said list into two parts:
([1, 1, 2], [3, 4, 4, 5, 1])"""
N = 3
la = [1, 1, 2, 3, 4, 4, 5, 1]
lb = la[:N] , la[N:]
print(lb)