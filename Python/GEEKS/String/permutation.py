"""Python Program to Count the Occurrences of Each Word in a Given String Sentence"""

from collections import Counter

string1 = input()
occur = Counter(char for char in string1 if char.isalpha())
print(occur)
print(len(occur))

"""Python Program to Count the Occurrences of Each Letter in a Given String Sentence"""

each_letter = Counter(string1.split()).most_common()
print(len(each_letter))

"""Python Program to make combination of any string"""

from itertools import permutations

string1 = input()
permutation = permutations(string1)

for p in permutation:
    print(p)
