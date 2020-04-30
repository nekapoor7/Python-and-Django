import re
def solution(A):
    if re.search('^\d{3}[-]\d{3}[-]\d{3}$',A):
        return "OK"
    else:
        return "Not OK"

A= input()
print(solution(A))