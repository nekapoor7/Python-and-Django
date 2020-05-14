"""Python Program to Check if a Substring is Present in a Given String"""

text = input()
text1= input()

res = [var for var in text1 if var in text]
print(res)

value = ''.join(res)
print(value)
if value in text:
    print("Found")
else:
    print("Not Found")

"""Python Program to Check if a String is a Palindrome or Not"""

text2 = input()
if text2 == text2[::-1]:
    print("Palindrome")
else:
    print("Not Palindrome")

"""Python Program to Form a New String where the First Character and the Last Character have been Exchanged"""

new_str = text2[-1:] + text2[1:-1] + text2[:1]
print(new_str)

"""Python Program to Form a New String Made of the First 2 and Last 2 characters From a Given String"""

new_string = text2[0:2]+text2[-2:]
print(new_string)