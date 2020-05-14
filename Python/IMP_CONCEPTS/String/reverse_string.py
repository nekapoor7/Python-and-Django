def reverse(seq):
    seqTrue = type(seq)
    emptyTrue = seqTrue()

    if seq == emptyTrue:
        return emptyTrue

    reverseq = reverse(seq[1:])
    firstseq = seq[0:1]

    result = reverseq + firstseq

    return result

string = str(input())
print(reverse(string))