"""Python Program to Count the Number of Vowels Present in a String using Sets"""
import re
text = str(input())

new_str = re.findall(r'[aeiouAEIOU]',text)
str1 = ''.join(new_str)

setA = set(str1)

print(len(setA))

