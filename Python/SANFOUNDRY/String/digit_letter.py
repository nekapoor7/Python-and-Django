"""Python Program to Calculate the Number of Digits and Letters in a String"""
import re

string_input = input()
string_input = string_input.lower()
digit_letter = len(re.findall(r'[0-9]',string_input))
letter_count = len(re.findall(r'[a-z]',string_input))
print(digit_letter)
print(letter_count)