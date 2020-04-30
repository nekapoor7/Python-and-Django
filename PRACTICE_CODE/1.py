def f(x):
    def f1(a,b):
        print("hello")
        if b == 0:
            print("No")
            return
        return f(a,b)
    return f1

@f
def f(a,b):
    return a % b
f(4,0)

#re.search(r'^('USD','CAD','GBP)\d{3}[,]+\w\d{3}[,]+[-+]?[0-9]*\.?[0-9]*[0-9]{3}[,]*$')