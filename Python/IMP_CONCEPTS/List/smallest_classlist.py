##Python program to find smallest number in a list

class Sort(object):

    def __init__(self,list1):
        self.list1 = list1

    @property
    def sort(self):
        for i in range(0,len(self.list1)-1):
            for j in range(0,len(self.list1)-1-i):
                if self.list1[j] > self.list1[j+1]:
                    temp = self.list1[j]
                    self.list1[j] = self.list1[j+1]
                    self.list1[j+1] = temp
        return self.list1

def main():
    obj = Sort([2,43,41,0,99])
    print(obj.sort)

if __name__ == "__main__":
    main()