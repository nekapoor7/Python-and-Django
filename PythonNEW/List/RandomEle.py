"""Write a Python program to extract a given number of randomly selected elements from a given list. Go to the editor
Original list:
[1, 1, 2, 3, 4, 4, 5, 1]
Selected 3 random numbers of the above list:
[4, 4, 1]"""
import random
l = [1, 1, 2, 3, 4, 4, 5, 1]
N = 3
ll = random.sample(l,N)
print(ll)