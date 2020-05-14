"""Write a Python program to sort a string lexicographically."""

a = ['B20', 'C20', 'D20', 'E20', 'F20', 'G20', 'H20', 'I20', 'J20',
     'K20', 'L20', 'M20', 'N20', 'O20', 'P20', 'Q20', 'R20', 'S20',
     'T20', 'U20', 'V20', 'W20', 'X20', 'Y20', 'Z20',
     'AA20', 'AB20', 'AC20', 'AD20', 'BA20', 'BB20', 'BC20', 'BD20']
a_str = str(a)

a1 = sorted(a,key=str.lower)
print(a1)

