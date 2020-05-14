'''num = input("Enter the number")
if (num == num[::-1]):
    print("Reverse Number")
else:
    print("Not reversed number")'''

def Reverse(seq):
    seqTrue = type(seq)
    emptyTrue = seqTrue()

    if seq == emptyTrue:
        return emptyTrue

    reverseq = Reverse(seq[1:])
    first = seq[0:1]

    result = reverseq + first

    return result

num = input("Enter the number")
print(Reverse(num))