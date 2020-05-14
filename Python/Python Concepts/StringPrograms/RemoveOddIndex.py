"""Write a Python program to remove the characters which have odd index values of a given string."""

class Remove:

    def __init__(self,string):
        self.string = string

    def getString(self):
        s1 = []
        for i in range(len(self.string)):
            if i % 2 != 0:
                s1.append(self.string[i])
        s2 = "".join(s1)
        return s2

if __name__ == "__main__":
    s = input()
    obj = Remove(s)
    s2 = obj.getString()
    print(s2)



