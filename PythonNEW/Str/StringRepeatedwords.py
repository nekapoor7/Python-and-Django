"""Write a Python program to find the first repeated word in a given string."""
"""Write a Python program to find the second most repeated word in a given string."""
"""from collections import Counter
s = input()
m = Counter(s.split())
print(m.most_common()[0][0])
print(m.most_common()[1][0])"""

from collections import Counter

def repeatedword(s):
    words = s.split()
    dict = Counter(words)

    for key in words:
        if dict[key] > 1:
            return key
            break

print(repeatedword('Ravi had been saying that he had been there'))