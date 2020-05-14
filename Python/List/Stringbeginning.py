"""Write a Python program to insert a given string at the beginning of all items in a list. Go to the editor
Sample list : [1,2,3,4], string : emp
Expected output : ['emp1', 'emp2', 'emp3', 'emp4']"""

l = [1,2,3,4]
print(['emp{0}'.format(i) for i in l])