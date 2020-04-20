#Python Program to Create a Class in which One Method Accepts a String from the User and Another Prints it

class Str():
    def __init__(self):
        self.string = ""
    def get(self):
        self.string = input("Enter the string")
    def put(self):
        print("String is")
        print(self.string)

obj = str()
obj.get()
obj.put()



