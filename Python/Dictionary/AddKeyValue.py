"""Write a Python script to add a key to a dictionary. Go to the editor

Sample Dictionary : {0: 10, 1: 20}
Expected Result : {0: 10, 1: 20, 2: 30}"""

l = int(input())
d = {}

for i in range(l):
    k = input()
    v = input()
    d.update({k:v})
print(d)