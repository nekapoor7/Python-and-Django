""" Basic calculator program using Python"""

class Calculator:

    def __init__(self,A,B):
        self.A = A
        self.B = B

    def add(self):
        return self.A + self.B

    def sub(self):
        return self.A - self.B

    def mult(self):
        return self.A * self.B

    def div(self):
        return self.A / self.B

n1, n2 = list(map(int, input().split()))
obj = Calculator(n1,n2)
print(obj.add())
print(obj.sub())
print(obj.mult())
print(obj.div())
