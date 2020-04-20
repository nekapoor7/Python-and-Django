#Reverse words in a given String in Python

def ReverseWord(string1):
    return ' '.join(word[::-1] for word in string1.split())

string1 = input()
print(ReverseWord(string1))