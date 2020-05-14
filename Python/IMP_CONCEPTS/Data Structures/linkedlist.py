class Node(object):

    def __init__(self,data):
        self.data = data
        self.next = None
        self.previous = None

    def get_data(self):
        return self.data

    def set_data(self,val):
        self.data = val

    def get_next(self):
        return self.next

    def set_next(self,val):
        self.next = val

    def get_previous(self):
        return self.previous

    def set_previous(self,val):
        set.previous = val

class List(object):

    def __init__(self):
        self.head = None

    def Add(self,val):
        tem = Node(val)
        tem.set_next(self.head)


