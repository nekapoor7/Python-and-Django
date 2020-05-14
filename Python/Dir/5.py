"""Write a Python program to convert a list into a nested dictionary of keys."""

l = ['1', '2', '3', '4', '5', '5', '5', '5', '56', '6', '6', '7', '7', '7', '8', '9']
a = b = {}
for i in l:
    b[i] = {}
    b = b[i]
print(a)

"""Write a Python program to sort a list alphabetically in a dictionary."""
d = {'ravi':'10','rajnish':'9','sanjeev':'15','yash':'2','suraj':'32','neha':'7','harsh':'25'}
dd = sorted(d.keys(),key=lambda x:x.lower())
d1 = dict(sorted(d.items(),key=lambda x:x[0].lower()))

for k, v in d1.items():
    print('{}:{}'.format(k,v),end=' ')

num = {'n1': [2, 3, 1], 'n2': [5, 1, 2], 'n3': [3, 2, 4]}
print(sorted(num.items(),key=lambda x:x[1],reverse=True))

"""Write a Python program to check multiple keys exists in a dictionary."""
m = [str(x) for x in input().split()]
if {key:value for key,value in d.items() if key in m}:
    print("Key Exist")
else:
    print("Key Not Exist")
