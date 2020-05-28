"""Write a Python program to create a list reflecting the modified run-length encoding from a given list of integers
 or a given list of characters. Go to the editor
Original list:
[1, 1, 2, 3, 4, 4, 5, 1]
List reflecting the modified run-length encoding from the said list:
[[2, 1], 2, 3, [2, 4], 5, 1]
Original String:
aabcddddadnss
List reflecting the modified run-length encoding from the said string:
[[2, 'a'], 'b', 'c', [4, 'd'], 'a', 'd', 'n', [2, 's']]"""
from itertools import groupby
def encoding(l):
    def run_length_encoding(l1):
        if len(l1) > 1:
            return [len(l1),l1[0]]
        else:
            return l1[0]
    return [run_length_encoding(list(group)) for key,group in groupby(l)]

print(encoding(input().split()))