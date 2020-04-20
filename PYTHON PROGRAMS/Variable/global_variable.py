def f():
    global s
    print(s)
    s = "Look for Geeksforgeeks Python Section"
    print(s)

s = "Global Variable"
f()
print(s)
