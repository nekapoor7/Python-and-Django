"""Write a Python program to flatten a shallow list."""

your_list =[[2,4,3],[1,5,6], [9], [7,9,0]]
l = [num for ele in your_list for num in ele]
print(l)

from itertools import chain
your_list = [[('video1',4)], [('video2',5),('video3',8)], [('video1',5)], [('video5', 7), ('video6',9)]]
new_list = list(chain(*your_list))
print(new_list)

