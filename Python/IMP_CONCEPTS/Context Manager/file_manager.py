class FileManager():

    def __init__(self,filename,mode):
        self.filename = filename
        self.mode = mode
        self.file = None

    def __enter__(self):
        self.file = open(self.filename,self.mode)
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.file.close()

# loading a file
with FileManager("C:\\Users\\nekapoor\\Python\PYTHON PROGRAMS\\file_data\\word.txt",'w') as f:
    f.write('Test')

print(f.closed)


