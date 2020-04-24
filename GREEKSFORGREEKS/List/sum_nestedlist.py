
def column_sum(list1):

    return sum(sum(x) if isinstance(x, list) else x for x in list1)


list1 = [1,3,5,6,[7,8]]
print(column_sum(list1))