with open("C:\\Users\\nekapoor\\Python\\file_data\\data.txt",'r',encoding='utf-8') as filename:
    line = filename.readline()

    while line != '':
        print(line,end = '')
        line = filename.readline()

filename.close()
