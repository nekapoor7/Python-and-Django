'''You are given three integers: , , and , respectively. Print two lines.
The first line should print the result of pow(a,b). The second line should print the result of pow(a,b,m). '''

a = int(input())
b= int(input())
m = int(input())
res = pow(a,b)
value = pow(a,b,m)
print(res)
print(value)


a = int(input())
b = int(input())
c = int(input())
d = int(input())
res = pow(a,b) + pow(c,d)
print(res)