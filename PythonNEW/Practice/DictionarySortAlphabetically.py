""" Write a Python program to sort a list alphabetically in a dictionary."""

d = {'ravi':'10','rajnish':'9','sanjeev':'15','yash':'2','suraj':'32','neha':'7','harsh':'25'}

d1 = dict(sorted(d.items(),key=lambda x:x[0].lower()))

for k, v in d1.items():
    print('{}:{}'.format(k,v),end=' ')