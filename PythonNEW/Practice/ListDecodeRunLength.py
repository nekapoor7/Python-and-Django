"""Write a Python program to decode a run-length encoded given list. Go to the editor
Original encoded list:
[[2, 1], 2, 3, [2, 4], 5, 1]
Decode a run-length encoded said list:
[1, 1, 2, 3, 4, 4, 5, 1]"""
from itertools import groupby
def decode(l):
    def run_length_encode(l1):
        if len(l1) > 1:
            return [len(l1),l1[0]]
        else:
            return l1[0]
    return [run_length_encode(list(group)) for key,group in groupby(l)]

print(decode(input().split()))