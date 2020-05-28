"""Python | Swap commas and dots in a String"""
import re
s = input()
ss = re.sub(',','.',s)
print(ss)