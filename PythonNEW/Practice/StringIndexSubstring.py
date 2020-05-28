""" Write a Python program to find the index of a given string at which a given substring starts.
If the substring is not found in the given string return 'Not found'."""

'''s = input()
c = input()
print([pos for pos, char in enumerate(s) if char == c])

s = 'shak#spea#e'
c = 's'
print([pos for pos, char in enumerate(s) if char == c])'''

'''import re

string = input()
pattern = input()
print(re.search(pattern, string).span()) ## this prints starting and end indices
print(re.search(pattern, string).span()[0]) ## this does what you wanted'''

def find_str(s,char):
    index = 0

    if char in s:
        c = char[0]
        for ch in s:
            if ch == c:
                if s[index:index+len(char)] == char:
                    return index
            index += 1
    return "Not Found"

print(find_str(input(),input()))