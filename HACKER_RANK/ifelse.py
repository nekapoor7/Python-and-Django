'''Task
Given an integer,

, perform the following conditional actions:

    If

is odd, print Weird
If
is even and in the inclusive range of to
, print Not Weird
If
is even and in the inclusive range of to
, print Weird
If
is even and greater than , print Not Weird'''

def Ifelse(num):
    if num % 2 == 0:
        if num >= 2 and num <= 5:
            print("Not Weird")
        elif num >=6 and num <= 20:
            print("Weird")
        elif num > 20 :
            print("Not Weird")
    else:
        print("Weird")

n = int(input("Enter the number"))
Ifelse(n)


