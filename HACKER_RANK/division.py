'''Task
Read two integers and print two lines. The first line should contain integer division, // .
The second line should contain float division, /

.

You don't need to perform any rounding or formatting operations. '''

def div(a , b):
    print( a // b)
    print ( a / b)


if __name__ == '__main__':
    a = int(input())
    b = int(input())
    div( a , b)