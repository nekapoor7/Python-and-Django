#Python Program to Check if a String is a Palindrome or Not

string = input()

if string == string[::-1]:
    print("Stirng is palindrome")
else:
    print("String is not Palindrome")