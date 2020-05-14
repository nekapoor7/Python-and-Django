#Python Program to Check if a Number is a Palindrome

num = int(input("Enter the number"))
rev = 0
temp = num

while (num > 0):
    dig = num % 10
    rev = (rev * 10) + dig
    num = num // 10
print(rev)
if(temp==rev):
    print("Palindrome")
else:
    print("Not Palimdrome")