def nextsquare():
    i = 1

    while True:
        yield i*i
        i += 1

limit = int(input("Enter the number"))
for num in nextsquare():
    if num > limit:
        break
    print(num)
