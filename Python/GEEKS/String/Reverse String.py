"""Reverse words in a given String in Python"""

def reverse(seq):
    SeqTrue = type(seq)
    emptyTrue = SeqTrue()

    if seq == emptyTrue:
        return emptyTrue

    revereSeq = reverse(seq[1:])
    firstSeq = seq[0:1]

    result = revereSeq + firstSeq
    return result

string1 = input()
seq = input()
print(reverse(seq))