"""Write a Python program to swap cases of a given string. Go to the editor
Sample Output:
pYTHON eXERCISES
jAVA
nUMpY"""

def stringswap(s):
    ns = s.swapcase()
    return ns

s = input()
print(stringswap(s))