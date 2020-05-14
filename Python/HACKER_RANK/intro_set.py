'''Input Format

The first line contains the integer,
, the total number of plants.
The second line contains the space separated heights of the plants.'''


def average(array):
    avg = set(array)
    return(sum(avg)/len(avg))

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)