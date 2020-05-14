def nextSquare(n):
   for i in range(n):
        if i < n:
            print(i**2)

if __name__ == '__main__':
    n = int(input())
    nextSquare(n)