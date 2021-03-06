class Fibonacci:

    def __init__(self):
        self.cache = {}

    def __call__(self, n):
        if n not in self.cache:
            if n == 0:
                self.cache[0] = 0
            elif n == 1:
                self.cache[1] = 1
            else :
                self.cache[n] = self.__call__(n-1) + self.__call__(n-2)
        return self.cache[n]

start = int(input())
end = int(input())
list1=[]
sum = 0
fib = Fibonacci()

for i in range(start,end + 1):
    list1.append(fib(i))
for ele in list1:
        sum += ele
print(list1)
print(sum)