"""Python Program to Form a New String where the First Character and the Last Character have been Exchanged"""

text = str(input())

new_string = text[-1:]+text[1:-1]+text[:1]

print(new_string)