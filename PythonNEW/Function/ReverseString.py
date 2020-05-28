""" Write a Python program to reverse a string. Go to the editor
Sample String : "1234abcd"
Expected Output : "dcba4321"""
def reverse(seq):
    typeseq = type(seq)
    emptyseq = typeseq()

    if emptyseq == seq:
        return emptyseq

    rev = reverse(seq[1:])
    first = seq[0:1]

    result = rev + first
    return result

l = input()
print(reverse(l))