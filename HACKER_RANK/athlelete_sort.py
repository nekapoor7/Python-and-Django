# !/bin/python3

import math
import os
import random
import re
import sys
from operator import itemgetter

mn = input().split()
m = int(mn[0])
n = int(mn[1])

arr = []

for _ in range(m):
    arr.append(list(map(int, input().rstrip().split())))

k = int(input())

sorted_arr = sorted(arr, key=itemgetter(k))

for row in sorted_arr:
    print(*row)