"""Write a Python program to match key values in two dictionaries. Go to the editor
Sample dictionary: {'key1': 1, 'key2': 3, 'key3': 2}, {'key1': 1, 'key2': 2}
Expected output: key1: 1 is present in both x and y"""

d = {'key1': 1, 'key2': 3, 'key3': 2}
l1 = {'key1': 1, 'key2': 2}

for (key,value) in set(d.items()) & set(l1.items()):
    print("%s:%s is present in both x and y" % (key,value))
