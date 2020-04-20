#Python Program to Copy the Contents of One File into Another(even lines)

'''with open("C:\\Users\\nekapoor\\Python\\file_data\\data.txt", 'r', encoding='utf-8') as filename:
    filename1 = open("C:\\Users\\nekapoor\\Python\\file_data\\data3.txt", "w+", encoding='utf-8')
    cont = filename.readline()
    type(cont)
    for i in range(0,len(cont)):
        if(i %2 != 0):
            filename1.write(cont[i])
        else:
            pass

filename1.close()

with open("C:\\Users\\nekapoor\\Python\\file_data\\data2.txt", 'r', encoding='utf-8') as filename1:
    cont = filename1.read()
    print(cont)

filename1.close()
filename.close()'''

# open file in read mode
fn = open('C:\\Users\\nekapoor\\Python\\file_data\\data.txt', 'r')

# open other file in write mode

fn1 = open('C:\\Users\\nekapoor\\Python\\file_data\\data4.txt', 'w')

# read the content of the file line by line
cont = fn.readlines()
type(cont)
for i in range(0, len(cont)):
    if (i % 2 != 0):
        fn1.write(cont[i])
    else:
        pass

# close the file
fn1.close()

# open file in read mode
fn1 = open('C:\\Users\\nekapoor\\Python\\file_data\\data4.txt', 'r')

# read the content of the file
cont1 = fn1.read()

# print the content of the file
print(cont1)

# close all files
fn.close()
fn1.close()
