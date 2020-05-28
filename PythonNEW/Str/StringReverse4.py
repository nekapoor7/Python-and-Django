"""Write a Python function to reverses a string if it's length is a multiple of 4. """


def reverse4(s):
        if len(s) % 4 == 0:
            ns = s[::-1]
            return ns
        else:
            return s

print(reverse4(input()))

'''def reverse4(seq):
    if len(seq) == 4:
        typeseq = type(seq)
        emptyseq = typeseq()

        if emptyseq == seq:
            return emptyseq

        rev = reverse4(seq[1:])
        first = seq[0:1]

        result = rev + first
        return result
    else:
        return seq

print(reverse4(input()))'''