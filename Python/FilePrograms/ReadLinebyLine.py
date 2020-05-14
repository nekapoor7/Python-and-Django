"""Write a Python program to read a file line by line and store it into a list."""

with open("C:\\Users\\nekapoor\\git\\Python-and-Django\\PYTHON PROGRAMS\\file_data\\nehacopy.txt", 'r',
              encoding='utf-8') as f:
    data = f.readlines()
    print(data)

'''def ReadLine(fname):
    with open("C:\\Users\\nekapoor\\git\\Python-and-Django\\PYTHON PROGRAMS\\file_data\\nehacopy.txt", 'r',
              encoding='utf-8') as f:
        content_list = f.readlines()
        print(content_list)

if __name__ == "__main__":
    fname = "C:\\Users\\nekapoor\\git\\Python-and-Django\\PYTHON PROGRAMS\\file_data\\nehacopy.txt"
    ReadLine(fname)'''