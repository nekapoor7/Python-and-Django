# Python program to print all
# prime number in an interval

start = int(input())
end = int(input())

for val in range(start,end + 1):
        if val > 1:
            for n in range(2,val):
                if (val % n) == 0:
                    break
            else:
                print(val,end=' ')