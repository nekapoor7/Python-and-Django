N = int(input())
list1 = list(map(int,input().split()))

for i in range(len(list1)-1):
    m_val = list1[i]
    for j in range(i+1,len(list1)):
        if list1[j] < m_val:
            m_val = list1[j]
    m_index = list1.index(m_val,i)
    if list1[i] != list1[m_index]:
        list1[i],list1[m_index] = list1[m_index],list1[i]

print(list1)