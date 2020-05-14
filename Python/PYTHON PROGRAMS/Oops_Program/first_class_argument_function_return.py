#Functions can return another function

def adder(x):
    def add(y):
        return x + y

    return add

add_obj = adder(15)

print(add_obj(15))