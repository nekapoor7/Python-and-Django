#Python Program to Put Even and Odd elements in a List into Two Different Lists

list1 = list(map(int, input("Enter the  numbers in a Given List").split()))

even_list = list(filter(lambda x : (x % 2 == 0), list1))

odd_list =  list(filter(lambda x : (x % 2 != 0), list1))

print("Even list",even_list)

print("Odd list",odd_list)