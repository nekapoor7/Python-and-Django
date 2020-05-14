class India():
    def capital(self):
        print("New Delhi")
    def language(self):
        print("Hindi")
    def type(self):
        print("Developing")

class USA():
    def capital(self):
        print("Washington D.C.")
    def language(self):
        print("English")
    def type(self):
        print("Developed")

def func(obj):
    obj.capital()
    obj.language()
    obj.type()

obj_india = India()
obj_usa = USA()

func(obj_india)
func(obj_usa)