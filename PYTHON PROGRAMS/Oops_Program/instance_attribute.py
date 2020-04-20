class Employee:

    def __init__(self):
        self.name = 'xyz'
        self.salary = 50000

    def show(self):
        print(self.name)
        print(self.salary)

emp = Employee()

print(vars(emp))
print(dir(emp))
