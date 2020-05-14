"""Write a Python program to remove the K'th element from a given list, print the new list. """
l = [1,1,2,3,4,4,5,1]
n = 3
'''r = [int(x) for x in input().split()]

ll = [v for i, v in enumerate(l) if i not in r]
print(ll)'''

nr = l[:n-1] + l[n:]
print(nr)

"""Write a Python program to extract a given number of randomly selected elements from a given list. Go to the editor
Original list:
[1, 1, 2, 3, 4, 4, 5, 1]
Selected 3 random numbers of the above list:
[4, 4, 1]"""

import random
l1 = [1, 1, 2, 3, 4, 4, 5, 1]
N = 3
l2 = random.sample(l1,N)
print(l2)
