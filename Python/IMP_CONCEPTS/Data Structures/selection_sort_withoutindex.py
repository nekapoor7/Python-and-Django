N = int(input())
list1 = list(map(int,input().split()))

for i in range(len(list1)):
    m_index = i
    for j in range(i+1,len(list1)):
        if list1[j] < list1[m_index]:
            m_index = j

    if list1[i] != list1[m_index]:
        list1[i],list1[m_index] = list1[m_index],list1[i]

print(list1)
