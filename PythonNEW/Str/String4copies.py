"""Write a Python function to get a string made of 4 copies of the last two characters
of a specified string (length must be at least 2). Go to the editor
Sample function and result :
insert_end('Python') -> onononon
insert_end('Exercises') -> eseseses"""

def insert_end(s):
    if len(s) >=2:
        ns = s[-2:] * 4
        return ns
    else:
        return s

print(insert_end(input()))