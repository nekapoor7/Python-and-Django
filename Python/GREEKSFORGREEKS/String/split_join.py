#Python program to split and join a string

def splitjoin(string):
    s = string.split(' ')
    print(s)
    str_join =  '-'.join(s)
    return str_join


string = input()
print(splitjoin(string))