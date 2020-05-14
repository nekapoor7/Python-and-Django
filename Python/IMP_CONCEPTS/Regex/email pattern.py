### Read a file and checks all the mail and write it to another file """"
import re

with open("C:\\Users\\nekapoor\\git\\Python-and-Django\\PYTHON PROGRAMS\\file_data\\data1.txt",'r',encoding='utf-8') as file1:
    data = file1.read()

with open("C:\\Users\\nekapoor\\git\\Python-and-Django\\PYTHON PROGRAMS\\file_data\\email1.txt", 'a+',encoding='utf-8') as file2:
    #print(data)

    e_regex = re.findall(r'\w+@\S+',data)
    #email_regex = " ".join(e_regex)
    for item in e_regex:
        item = item.strip('[]')
        print(item)

    if len(item) > 0:
        file2.write(item+"\r\n")




