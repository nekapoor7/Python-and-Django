# Python3 Program to
# find sum of square
# of first n natural
# numbers

def naturalsum(n):
    return (n * (n + 1) * (2 * n + 1)) // 6

num = int(input())
print(naturalsum(num))