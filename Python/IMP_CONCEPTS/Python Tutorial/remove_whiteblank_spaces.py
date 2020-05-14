import logging

data = []
clean_data = []
clean_data_1 = []

with open('C:\\Users\\nekapoor\\git\\Python-and-Django\\PYTHON PROGRAMS\\file_data\\data1.txt','r') as filename:
    data = filename.readlines()
    print(data)
    for x in data:
        print(x.strip())
        val = x.strip()
        clean_data.append(val)
        clean_data_1 = list(filter(''.__ne__,clean_data))
    print(clean_data)
    print(clean_data_1)
