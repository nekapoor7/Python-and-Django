class file_method():
    def __init__(self,filename,mode):
        self.filename = filename
        self.mode = mode


    def __enter__(self):
        self.filename = open(self.filename)

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.file.close()

with open("data.txt",'w',encoding='utf-8') as f:
    f.write('Neha Kapoor')
