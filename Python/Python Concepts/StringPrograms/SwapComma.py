"""Write a Python program to swap comma and dot in a string. Go to the editor
Sample string: "32.054,23"
Expected Output: "32,054.23"""
import re
s = input()

s1 = s.translate(', .', '., ')
print(s1)