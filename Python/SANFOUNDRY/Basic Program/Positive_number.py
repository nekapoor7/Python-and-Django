"""Python Program to Check Whether a Number is Positive or Negative"""

def pos_neg(num):
    while num > 0:
        return "Positive"
    else:
        return "Negative"

num = int(input())
print(pos_neg(num))