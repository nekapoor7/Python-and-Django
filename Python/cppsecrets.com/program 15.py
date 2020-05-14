"""Python Program to Check if a Substring is Present in a Given String"""

text = input()
text1 = input()

result = [val for val in text1 if val in text]
substr = ''.join(result)

if substr in text:
    print("Substring is Present")
else:
    print("Substring is not Present")