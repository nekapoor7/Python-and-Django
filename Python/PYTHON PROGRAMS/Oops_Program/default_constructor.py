class default_const:
    var = ""

    def __init__(self):
        self.var = "Variable"

    def print_var(self):
        print(self.var)

obj = default_const()

obj.print_var()