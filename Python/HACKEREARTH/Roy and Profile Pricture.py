l = int(input())
n = int(input())
for i in range(0, n):
    x = list(map(int, input().split(" ")))

    if x[0] < l or x[1] < l:
        print("UPLOAD ANOTHER")
    elif x[0] == x[1] and x[0] >= l:
        print("ACCEPTED")
    else:
        print("CROP IT") 