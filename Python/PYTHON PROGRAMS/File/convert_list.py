#
with open("C:\\Users\\nekapoor\\Python\\file_data\\word.txt", 'r', encoding='utf-8') as f1:
    for line in f1:
        print(line,end='')

li = [i.strip().split() for i in open("C:\\Users\\nekapoor\\Python\\file_data\\word.txt").readlines()]
'''result = [line.split() for line in f1]
print(result)'''
print(li)
f1.close()