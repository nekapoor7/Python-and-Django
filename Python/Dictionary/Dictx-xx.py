"""Write a Python script to generate and print a dictionary that contains a number
(between 1 and n) in the form (x, x*x). Go to the editor
Sample Dictionary ( n = 5) :
Expected Output : {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}"""

n = int(input())
d = {x:x*x for x in range(1,n+1)}

print(d)

"""Write a Python script to print a dictionary where the keys are numbers 
between 1 and 15 (both included) and the values are square of keys. Go to the editor
Sample Dictionary
{1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81, 10: 100, 11: 121, 12: 144, 13: 169, 14: 196, 15: 225}"""

n,n1 = list(map(int,input().split()))
d1 = {x:x*x for x in range(n,n1+1)}
print(d1)