"""Q13. Given two strings s and t , write a function to determine if t is an anagram of s.

Example 1:

Input: s = "anagram", t = "nagaram"
Output: true

Example 2:

Input: s = "rat", t = "car"
Output: false

Note:
You may assume the string contains only lowercase alphabets.

"""
def Anagram(t,s):
    if sorted(t) == sorted(s):
        return True
    else:
        return False

t = input()
s = input()
print(Anagram(t,s))