'''The first line consists of an integer, , the size of each group.
The second line contains the unordered elements of the room number list.'''


k,arr = int(input()),list(map(int, input().split()))

myset = set(arr)

print(((sum(myset)*k)-(sum(arr)))//(k-1))