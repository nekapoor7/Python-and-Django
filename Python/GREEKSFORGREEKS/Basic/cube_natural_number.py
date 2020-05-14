# A formula based Python program to find sum
# of series with cubes of first n natural
# numbers

def sumOfSeries(n):
    x = (n * (n + 1) / 2)
    return (int)(x*x)

num = int(input())
print(sumOfSeries(num))