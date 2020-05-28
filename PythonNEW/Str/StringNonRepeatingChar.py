"""Write a Python program to find the first non-repeating character in given string."""

def nonrepeatingchar(word):
    return sorted(word,key=lambda x:(word.count(x),word.index(x)))[0]

print(nonrepeatingchar(input()))