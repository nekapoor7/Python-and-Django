"""Python Program to Check if a Number is a Palindrome"""

'''num = int(input())
rev = 0

while num > 0:
    digit = num % 10
    rev = rev * 10 + digit
    num = num // 10

print(rev)
if num == rev:
    print("Palindrome")
else:
    print("Not Palindrome")'''

n=int(input("Enter number:"))
temp=n
rev=0
while(n>0):
    dig=n%10
    rev=rev*10+dig
    n=n//10
if(temp==rev):
    print("The number is a palindrome!")
else:
    print("The number isn't a palindrome!")