'''Read an integer

.

Without using any string methods, try to print the following:

Note that "" represents the values in between. '''

def number(num):
    for i in range(1,num+1):
        print(i,end="")



if __name__ == '__main__':
    n = int(input())
    number(n)