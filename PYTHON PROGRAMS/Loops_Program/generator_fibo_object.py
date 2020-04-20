def genertor_object():

    a , b = 0 , 1
    while True:
        yield a
        a , b = b , a + b

fib = genertor_object()

n = int(input("Enter the limit"))
for i in fib:
    if i > n:
        break
    else:
        print(i)