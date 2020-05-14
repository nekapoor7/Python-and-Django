def solution(A):
    # write your code in Python 3.6
    B = set(A)
    ans = 1
    while ans in B:
       ans += 1
    return ans


list1 = list(map(int,input().split()))
print(solution(list1))