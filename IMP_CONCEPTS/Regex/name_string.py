import re

nameage = '''
Janice is 22 and Theon is 33
Gabriel is 44 and Joey is 22
'''

ages = re.findall(r'\d{1,3}',nameage)
names = re.findall(r'[A-Z][a-z]*',nameage)

mydict= {}
x = 0

for each in names:
    mydict[each] = ages[x]
    x += 1
print(mydict)