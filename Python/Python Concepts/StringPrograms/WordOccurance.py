"""Write a Python program to count the occurrences of each word in a given sentence."""
from collections import Counter
'''from itertools import chain
from collections import Counter
from nltk.tokenize import sent_tokenize, word_tokenize

text = input()
wordlist = list(chain(*[word_tokenize(s) for s in sent_tokenize(text)]))
print(Counter(wordlist))'''

s = input()
w_count = dict(Counter(s.split()))
print(w_count)


