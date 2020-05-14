"""Write a Python program to reverse a string."""

def reverse(seq):
    typeseq = type(seq)
    emptyseq = typeseq()

    if emptyseq == seq:
        return emptyseq

    rev = reverse(seq[1:])
    first = seq[0:1]

    result = rev + first
    return result

s = input()
print(reverse(s))