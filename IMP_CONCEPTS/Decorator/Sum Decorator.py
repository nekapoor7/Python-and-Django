def sum_decorator(func):
    def inner(*args,**kwargs):

        print("Before Execution")

        return_value = func( *args, **kwargs)
        print("After execution")

        return return_value

    return inner


@sum_decorator
def sum_func(n1,n2):
    return n1 + n2

num1 ,num2 = 2,4
print("The sum of 2 numbers",sum_func(num1,num2))