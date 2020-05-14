#Python Program to Copy the Contents of One File into Another

#open 1st file
with open("C:\\Users\\nekapoor\\Python\\file_data\\data.txt", 'r', encoding='utf-8') as filename:
    with open("C:\\Users\\nekapoor\\Python\\file_data\\data1.txt", 'w', encoding='utf-8') as filename1:
        cont = filename.readlines()
        type(cont)
        for i in range(0,len(cont)):
            filename1.write(cont[i])
            pass

filename1.close()

with open("C:\\Users\\nekapoor\\Python\\file_data\\data1.txt", 'r', encoding='utf-8') as filename1:
    cont1 = filename1.read()
    print(cont1)

filename.close()
filename1.close()