#Merge Sort

def merge(leftList,rightList):

    leftListIndex = 0
    rightListIndex = 0
    leftListLength = len(leftList)
    rightListLength = len(rightList)
    originalLength = leftListLength + rightListLength
    sorted_list = []

    for _ in range(0,originalLength):

        if leftListIndex < leftListLength and rightListIndex < rightListLength:

            if leftList[leftListIndex] <= rightList[rightListIndex]:
                sorted_list.append(leftList[leftListIndex])
                leftListIndex = leftListIndex + 1

            else:
                sorted_list.append(rightList[rightListIndex])
                rightListIndex = rightListIndex + 1

        elif leftListIndex == leftListLength:
            sorted_list.append(rightList[rightListIndex])
            rightListIndex = rightListIndex + 1

        elif rightListIndex == rightListLength:
            sorted_list.append(leftList[leftListIndex])
            leftListIndex = leftListIndex + 1

    return sorted_list

def merge_sort(list1):
    if len(list1) <= 1:
        return list1
    else:
        mid = len(list1) // 2
        leftList = merge_sort(list1[:mid])
        rightList = merge_sort(list1[mid:])

        return merge(leftList,rightList)

if __name__ == "__main__":
    list1 = merge_sort([1,2,2,1,4,1,6,2,4])
    print(list1)



