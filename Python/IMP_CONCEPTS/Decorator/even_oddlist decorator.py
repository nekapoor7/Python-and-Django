#Checking Arguments with a Decorator

def Even_Odd_In_A_List(func):
    def helper(list1):
        if len(list1) > 1:
            return func(list1)
        else:
            raise Exception("List has contain only single element")
    return helper


@Even_Odd_In_A_List
def even_odd(list1):
    even_list = list(filter(lambda Varx : Varx % 2 == 0,list1))
    return even_list


list1 = list(map(int,input().split()))
print(even_odd(list1))