import threading

def add(a,b):
    result = a + b
    return result

for i in range(5):
    t = threading.Thread(target=add, args=(10, 20))
    t.start

num1 = int(input())
num2 = int(input())
print(add(num1,num2))