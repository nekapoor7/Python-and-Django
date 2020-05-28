"""Write a Python program to read first n lines of a file."""
import itertools

f = open('C:\\Users\\nekapoor\\git\\Python-and-Django\\PYTHON PROGRAMS\\file_data\\data.txt','r')
N = int(input())

for line in itertools.islice(f,N):
    print(line)
