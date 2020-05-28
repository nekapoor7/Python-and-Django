"""Write a Python function to reverses a string if it's length is a multiple of 4. """

def Reverse(seq):
    if len(seq) % 4 == 0:
        typeseq = type(seq)
        emptyseq = typeseq()

        if emptyseq == seq:
            return emptyseq

        rev = Reverse(seq[1:])
        first = seq[0:1]

        result = rev + first
        return result
    else:
        return seq

s = input()
print(Reverse(s))