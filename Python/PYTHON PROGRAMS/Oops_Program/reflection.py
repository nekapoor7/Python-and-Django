'''def reverse(seq):

    seqtype = type(seq)
    emptyseq = seqtype()

    if seq == emptyseq:
        return emptyseq

    restrev = reverse(seq[1:])
    first = seq[0:1]

    result = first + restrev

    return result

print(reverse([1, 2, 3, 4]))
print(reverse("HELLO"))'''


def reverse(seq):
    SeqType = type(seq)
    emptySeq = SeqType()

    if seq == emptySeq:
        return emptySeq

    restrev = reverse(seq[1:])
    first = seq[0:1]

    # Combine the result
    result = restrev + first

    return result


# Driver code
print(reverse([1, 2, 3, 4]))
print(reverse("HELLO"))