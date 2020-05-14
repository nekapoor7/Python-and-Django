"""Write a Python program to read first n lines of a file."""

def lastnlines(fname,N):
    with open("C:\\Users\\nekapoor\\git\\Python-and-Django\\PYTHON PROGRAMS\\file_data\\data_copy.txt",'r',encoding='utf-8') as f:
        for line in (f.readlines()[-N:]):
            print(line,end='')

if __name__ == "__main__":
    fname ="C:\\Users\\nekapoor\\git\\Python-and-Django\\PYTHON PROGRAMS\\file_data\\data_copy.txt"
    N = int(input())
    try:
        lastnlines(fname,N)
    except:
        print('File not Found')

