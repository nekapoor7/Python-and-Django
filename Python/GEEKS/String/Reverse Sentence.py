"""Reverse a Sentence of a String"""

def reverseSentence(string1):

    words = string1.split(' ')

    sentence = ' '.join(reversed(words))

    return sentence

string1 = str(input())
print(reverseSentence(string1))