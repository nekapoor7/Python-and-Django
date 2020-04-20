'''Akash and Vishal are quite fond of travelling. They mostly travel by railways. They were travelling in a train one day and they got interested in the seating arrangement of their compartment. The compartment looked something like


So they got interested to know the seat number facing them and the seat type facing them. The seats are denoted as follows :

    Window Seat : WS
    Middle Seat : MS
    Aisle Seat : AS

You will be given a seat number, find out the seat number facing you and the seat type, i.e. WS, MS or AS.

INPUT
First line of input will consist of a single integer T denoting number of test-cases. Each test-case consists of a single integer N denoting the seat-number.

OUTPUT
For each test case, print the facing seat-number and the seat-type, separated by a single space in a new line.

CONSTRAINTS

    1<=T<=105
    1<=N<=108'''


test_case= int(input())
for i in range(0,test_case):
    s=int(input())
    if s%12==0 or s%12==1:
        if s%12==0:
            print(s-11, 'WS')
        else:
            print(s+11, 'WS')
    elif s%12==6 or s%12==7:
        if s%12==6:
            print(s+1, 'WS')
        else:
            print(s-1, 'WS')
    elif s%12==2 or s%12==11:
        if s%12==2:
            print(s+9, 'MS')
        else:
            print(s-9, 'MS')
    elif s%12==5 or s%12==8:
        if s%12==5:
            print(s+3, 'MS')
        else:
            print(s-3, 'MS')
    elif s%12==3 or s%12==10:
        if s%12==3:
            print (s+7, 'AS')
        else:
            print(s-7, 'AS')
    else:
        if s%4==0:
            print(s+5, 'AS')
        else:
            print(s-5, 'AS')