class Student:

    # Class Variable
    stream = 'cse'

    # The init method or constructor
    def __init__(self,roll):

        #Instance variable
        self.roll = roll

    #Adds an instance variable
    def setAdress(self,address):
        self.address = address

    #Retrieve an instance variable
    def getaddress(self):
        return self.address

a = Student(101)
a.setAdress("Noida , UP ")
print(a.getaddress())