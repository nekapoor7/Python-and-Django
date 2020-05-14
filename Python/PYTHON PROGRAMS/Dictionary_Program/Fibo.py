#Python program to generate Fibonacci series until 'n' value
n = int(input("Enter the value of 'n': "))
n2 = int(input("Enter the value of 'n': "))
a = 0
b = 1
sum = 0
count = 1
print("Fibonacci Series: ", end = " ")
for i in range(n,n2):
  print(sum, end = " ")
  count += 1
  a = b
  b = sum
  sum = a + b