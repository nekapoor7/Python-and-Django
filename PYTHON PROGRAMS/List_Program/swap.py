def sorted_list(list1):

    list1[0], list1 [-1] = list1[-1], list1[0]

    return list1


list1 = list(map(int ,input("Enter the multiple values").split()))
print(sorted_list(list1))
