#Python Program to Reverse a Given Number

num = int(input("Enter the number"))
rev = 0
dig = 0

while (num > 0):
    dig = num % 10
    rev = (rev * 10) + dig
    num = num // 10

print(rev)

