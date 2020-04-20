#Python Program to reverse the string

def reverse(seq):
    seqTrue = type(seq)
    emptyTrue = seqTrue()

    if seq == emptyTrue:
        return emptyTrue

    reverseq = reverse(seq[1:])
    first = seq[0:1]

    result = reverseq + first
    return result

string = str(input("Enter the string"))
print(reverse(string))