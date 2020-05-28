"""Write a Python script to add a key to a dictionary. Go to the editor

Sample Dictionary : {0: 10, 1: 20}
Expected Result : {0: 10, 1: 20, 2: 30}"""

d = {}
N = int(input())

for i in range(N):
    key = input()
    value = input()
    d.update({key:value})
print(d)
