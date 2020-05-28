"""Write a Python program to split a list based on first character of word."""
from operator import itemgetter
from itertools import groupby
word_list = ['be','have','do','say','get','make','go','know','take','see','come','think',
     'look','want','give','use','find','tell','ask','work','seem','feel','leave','call']

for letter,words in groupby(sorted(word_list),key=itemgetter(0)):
    print(letter)
    for word in words:
        print(word)