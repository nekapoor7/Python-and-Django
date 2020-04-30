"""Find length of a string in python (4 ways)"""

'''string1 = input()
count = 0

for i in string1:
    count += 1

print(count)'''

import re

def solution(A):
    result = re.findall(r'[a-zA-Z]',A)
    return len(result)

A = input()
print(solution(A))