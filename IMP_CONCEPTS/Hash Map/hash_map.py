class HashTable(object):

    def __init__(self):
        self.size = 10
        self.arr = [None for i in range(self.size)]

    def get_hash(self,key,value):
        h = 0
        for char in key:
            h += ord(char)
        return value

    def __setitem__(self, key, value):
        h = self.get_hash(key)
        self.arr[h] = value

    def __getitem__(self, key):
        h = self.get_hash(key)
        return self.arr[h]

    def print(self):
        print(self.arr)

if __name__ == "__main__":
    t = HashTable()
    t.get_hash('Neha','7')
    t.get_hash('harsh', '10')
    t.print()




