num1 = int(input("Enter the first number"))
num2 = int(input("Enter the second number"))

'''if num1 > num2 :
    small = num2
else:
    small = num1

for i in range(1,small+1):
    if ((num1 % i == 0) and (num2 % i == 0)):
        gcd = i

print("GCD of 2 number",gcd)'''

#Euclidean Algorithm

while(num2):
    num1 , num2 = num2 , num1 % num2

print ("The gcd of 2 numbers are : ",num1,end="")