def reverse(seq):
    seqtype = type(seq)
    emptyseq = seqtype()

    if seq == emptyseq:
        return emptyseq

    reverseq = reverse(seq[1:])
    first = seq[0:1]

    result = reverseq + first

    return result

string = str(input("Enter the string"))
print(reverse(string))
