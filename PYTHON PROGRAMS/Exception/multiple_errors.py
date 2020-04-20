## Program to handle multiple errors with one except statement

try:
    a = 2
    if a < 4:
        b = a/(a-3)

    print("Value of b = ",b)

except (ZeroDivisionError,NameError):
    print("\nError Occurred and Handled")