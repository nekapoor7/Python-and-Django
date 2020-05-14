"""Write a Python script to sort (ascending and descending) a dictionary by value. """
from collections import OrderedDict
from operator import itemgetter
d = {'ravi':'10','rajnish':'9','sanjeev':'15','yash':'2','suraj':'32','neha':'7','harsh':'25'}

k = OrderedDict(sorted(d.items(),reverse=True))
k1 = OrderedDict(sorted(d.items()))

print(k)
print(k1)

l = {key:int(value) for key,value in d.items()}
k2 = OrderedDict(sorted(l.items(),key=itemgetter(1)))
print(k2)
k3 = OrderedDict(sorted(l.items(),key=itemgetter(1),reverse=True))
print(k3)

"""Write a Python script to add a key to a dictionary. Go to the editor

Sample Dictionary : {0: 10, 1: 20}
Expected Result : {0: 10, 1: 20, 2: 30}"""

'''N = int(input())
d = {}
for i in range(N):
    k = input()
    v = input()
    d.update({k:v})
print(d)'''

"""Write a Python script to concatenate following dictionaries to create a new one. Go to the editor

Sample Dictionary :
dic1={1:10, 2:20}
dic2={3:30, 4:40}
dic3={5:50,6:60}
Expected Result : {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}"""

dic1={1:10, 2:20}
dic2={3:30, 4:40}
dic3={5:50,6:60}
d1 = {**dic1,**dic2,**dic3}
print(d1)

"""Write a Python script to check whether a given key already exists in a dictionary. """
la = input()
if la in d:
    print("Key Exist",d[la])
else:
    print("Key Not Found")

"""Write a Python script to generate and print a dictionary that contains a number 
(between 1 and n) in the form (x, x*x). Go to the editor
Sample Dictionary ( n = 5) :
Expected Output : {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}"""
N = int(input())
d = {x:x*x for x in range(1,N+1)}
print(d)

"""Write a Python script to print a dictionary where the keys are numbers
 between 1 and 15 (both included) and the values are square of keys. Go to the editor
Sample Dictionary
{1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81, 10: 100, 11: 121, 12: 144, 13: 169, 14: 196, 15: 225}"""
N,N1 = list(map(int,input().split()))
d = {x:x*x for x in range(N,N1+1)}
print(d)