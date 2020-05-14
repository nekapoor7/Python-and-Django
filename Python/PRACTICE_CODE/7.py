
import re
def solution(A):
    A = A.lower()
    if re.findall(r't.*?[^e]a$',A):
        return "OK"
    else:
        return "Not OK"

A = input()
print(solution(A))