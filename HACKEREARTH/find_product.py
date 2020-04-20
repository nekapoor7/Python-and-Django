'''You have been given an array A of size N consisting of positive integers. You need to find and print the product of all the number in this array Modulo

.

Input Format:
The first line contains a single integer N denoting the size of the array. The next line contains N space separated integers denoting the elements of the array

Output Format:
Print a single integer denoting the product of all the elements of the array Modulo

.

Constraints:

'''

# Write your code here
def factorial(num):
    if num == 1 or num == 0:
        return 1
    else:
        return num * factorial(num-1)

num = int(input())
print(factorial(num))