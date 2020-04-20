class Test:
    def __init__(self,num1):
        self.var = 10
        self._var1 = 100
        self.__var2 = 200
        self.num1 = num1

    def __add__(self, other):
        t = []
        for x , y in zip(self.num1,other.num1):
            #print(x + y)
            t.append(x+y)
        return t
         #return self.num1 + other.num1

    def get_var2(self):
        return self.__var2

    def setter_var2(self,num):
        self.__var2 = num

    def func(self):
        print(self.var)
        print(self._var1)
        print(self.__var2)

    def _func(self):
        print(self.var)
        print(self._var1)
        print(self.__var2)


if __name__ == "__main__":
    '''t = Test()
    t.func()
    print(t.get_var2())
    print(t.setter_var2(55))
    print(t.get_var2())'''

    '''T1 = Test(num1=10)
    T2 = Test(num1=22)
    print("Operation Added",T1 + T2)'''

    list1 = list(map(int,input().split()))
    list2 = list(map(int,input().split()))

    L1 = Test(num1=list1)
    L2 = Test(num1=list2)
    print("Addition of two lists",L1 + L2,end=' ')
