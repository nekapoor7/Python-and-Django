import re
N = int(input())
number = [input() for i in range(N)]
check = lambda no:len(re.findall("^[7-9]\d{9}$",no))
match = map(check, number)

for i in match:
    if i == 1:
        print ("YES")
    else:
        print ("NO")