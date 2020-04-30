"""Python | Reverse each word in a sentence"""

def ReverseEachWord(string1):
    return ' '.join(word[::-1] for word in string1.split(" "))

string1 = input()
print(ReverseEachWord(string1))