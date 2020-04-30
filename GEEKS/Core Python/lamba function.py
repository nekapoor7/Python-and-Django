"""Lambda function

A function without name is called lambda function.

Anonymous function are not defined using def keyword rather they are defined using lambda keyword.
"""

sum = lambda x : x + 1
print(sum(5))

add = lambda x , y : x + y
add((5,2))

"""
1. Lambda Function doesn't have any name.
2. Lambda function returns a fucntion
3. function can take zero or any number of argument but contains only one expression.
4. in lambda function there is no need to write return statement."""