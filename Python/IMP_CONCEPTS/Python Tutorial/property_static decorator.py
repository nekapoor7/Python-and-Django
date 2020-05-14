class Test:

    myvar = 22222

    def __init__(self,num=1):
        self.num = num
        self.__num = 122

    def get_value(self):
        return self.__num

    def set_value(self,num):
        self.__num = num

    @property
    def methodA(self):
        print("Hi I am Method A")

    @staticmethod
    def methodB():
        print("I am method B")

    def __str__(self):
        return "Object Test"

    def classvaraccess(cls):
        print("Class variable access {} ".format(cls.myvar))

if __name__ == "__main__":
    obj = Test()
    print(obj)
    print(obj.methodA)
    print(obj.methodB())
    print(obj.classvaraccess())
