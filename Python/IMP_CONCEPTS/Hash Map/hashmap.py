class HashMap(object):

    def __init__(self):
        self.size = 10
        self.bucket = [None] * self.size
        print(self.bucket)

    def hashFunction(self,key):
        Hash = 0
        for char in key:
            Hash += ord(char)
        return Hash % self.size

    def Add(self, key, value):
        KeyHashIndex = self.hashFunction(key)

        arr = [key,value]

        if self.bucket[KeyHashIndex] is None:
            self.bucket[KeyHashIndex] = list([arr])
            return True
        else:
            """
            [
            ["apple","Apple"]
            """
            for pair in self.bucket[KeyHashIndex]:
                if pair[0] == key:
                    pair[1] = value          # Its going to replace value
                else:
                    pass
            self.bucket[KeyHashIndex].append(arr)
            return True

    def print(self):
        print(self.bucket)

if __name__ == "__main__":
    d = HashMap()
    '''num = d.hashFunction("apple")
    num1 = d.hashFunction("name")
    num3 = d.hashFunction("harsh")
    print(num,num1,num3)'''
    d.Add("name","neha")
    d.print()


