"""Write a Python program to read first n lines of a file."""

def firstnlines(fname,N):
    with open("C:\\Users\\nekapoor\\git\\Python-and-Django\\PYTHON PROGRAMS\\file_data\\data.txt", 'r',
              encoding='utf-8') as f:
        for lines in (f.readlines()[:N]):
            print(lines,end='')

if __name__ == "__main__":
    fname = "C:\\Users\\nekapoor\\git\\Python-and-Django\\PYTHON PROGRAMS\\file_data\\data.txt"
    N = int(input())
    try:
        firstnlines(fname,N)
    except:
        print('File Not Found')