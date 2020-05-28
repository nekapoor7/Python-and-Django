"""Write a Python program to change the position of every n-th value with the (n+1)th in a list. Go to the editor
Sample list: [0,1,2,3,4,5]
Expected Output: [1, 0, 3, 2, 5, 4]"""


'''def change_pos(my_list):
    for i in range(0, len(my_list), 2):
        my_list[i], my_list[i + 1] = my_list[i + 1], my_list[i]
        print(my_list)
        return'''

my_list = [0, 1, 2, 3, 4, 5]

for i in range(0,len(my_list),2):
    my_list[i],my_list[i + 1] = my_list[i + 1],my_list[i]
print(my_list)