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

obj_india  = India()
obj_usa = USA()

for country in (obj_india,obj_usa):
    country.capital()
    country.language()
    country.type()