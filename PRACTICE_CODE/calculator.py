#Python Program to Create a Class which Performs Basic Calculator Operations

class Calculator:
    def __init__(self,a,b):
        self.a = a
        self.b = b
    def add(self):
        return self.a + self.b
    def subtract(self):
        return self.a - self.b
    def multiply(self):
        return self.a * self.b
    def divide(self):
        return self.a / self.b

num1 = int(input("Enter the first number"))
num2 = int(input("Enter the second number"))
obj = Calculator(num1,num2)
print("Result: ",obj.add())
print("Result: ",obj.subtract())
print("Result: ",obj.divide())
print("Result: ",obj.multiply())