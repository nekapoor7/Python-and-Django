'''Given an integer, , print the following values for each integer from to:

    Decimal
    Octal
    Hexadecimal (capitalized)
    Binary

The four values must be printed on a single line in the order specified above for each
from to . Each value should be space-padded to match the width of the binary value of .'''

def print_formatted(number):
    width = len("{0:b}".format(number))

    for i in range(1, number + 1):
        print("{0:{w}d} {0:{w}o} {0:{w}X} {0:{w}b}".format(i, w = width))


if __name__ == '__main__':
    n = int(input())
    print_formatted(n)