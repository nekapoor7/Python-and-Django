class India:
    def capital(self):
        print("New Delhi")
        
    def language(self):
        print("Hindi")
        
    def type(self):
        print("Developing")
        
class USA:
    def capital(self):
        print("Washington D.C.")

    def language(self):
        print("English")

    def type(self):
        print("Developed")

obj_India = India()
obj_USA = USA()

for country in (obj_India,obj_USA):
    country.capital()
    country.language()
    country.type()

