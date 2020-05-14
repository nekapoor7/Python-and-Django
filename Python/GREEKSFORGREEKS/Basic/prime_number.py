num = int(input())
if num > 1:
    for i in range(2,num):
        if (num % i) == 0:
            print(num , "Its not a prime number")
            #print(i, "times", num // i, "is", num)
            break
    else:
        print(num, "Its a Prime Number")
else:
    print(num, "Its not a Prime Number")
