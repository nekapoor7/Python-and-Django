def create_adder(x):
    def nested_adder(y):
        return x + y

    return nested_adder

add_15 = create_adder(15)

print(add_15(20))