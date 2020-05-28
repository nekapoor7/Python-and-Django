"""Python | Check for URL in a String"""
import re
s = input()
print(re.findall(r'(https?://[^\s]+)',s))