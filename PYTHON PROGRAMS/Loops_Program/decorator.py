def functional_decorater(func):
    func.data = 3
    return func

@functional_decorater
def add(x , y):
    return x + y

print(add(2,3))
print(add.data)