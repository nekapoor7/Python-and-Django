# Python program to show that we can create
# instance variables inside methods

class Student:

    #class variable
    stream = 'cse'

    def __init__(self,roll):
        self.roll = roll
        #instance variable

    def setAddress(self,address):
        self.address = address

    def getAddress(self):
        return self.address

# Driver Code
a = Student(101)
a.setAddress("Noida, UP")
print(a.getAddress())