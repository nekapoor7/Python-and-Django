N = int(input())
list1 = list(map(int,input().split()))

tup = tuple(list1)
tuple_list = list(tup)

d = {
    "key": "val1",
    "key1": "val2"
}

print(list(d.keys()))
print(list(d.values()))

list2 = list(map(int,input().split()))
list3 = list(map(str,input().split()))

d_dict = dict (
    zip(
        list2,list3
    )
)

d_tuple = tuple(
    zip(
        list2,list3
    )
)

print(list2,list3)
print(d_dict)
print(d_tuple)

print(tup)
print(tuple_list)
