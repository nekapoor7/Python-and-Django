""" Set and FrozenSet

Set --> unordered -> no duplicate
builtin funciton set()

set1 = set()

set1 = 'neha'
{'a','e','h','n'}

Frozen set -> Immutable Objects, elements can be modified -> iterable object

Dictionary ->

Student = { 'name': 'neha', 'educ':'MCA','college' : 'BITS Mesra'}
key = frozenset(Student)

output -> keys --> {'name','educ','college'}


--------------

2.

var x = 10
var y = 10   --> Interger ( 10 -> x -> addrsss  10-> y -> address )
Pass/call object by reference list1 = [1,2,3] , def Add(l) --> l.append(4) --> [1,2,3] --> Adress [1,2,3,4] --> Address == List1 [1,2,3]

list1 =[1,2,3]   --> [1,2,3] Address --> [1,2,3] --> Differnce Address
list2 = [1,2,3]

--------------------------------------------------

3.

membership operator list1 is list2  is -> operator same object or not

if (list1 is list2) --> False
var x = 10
var y = 10

if (x is y)  --> True


4. dict.keys()
   sorted(Orderdict,dict.items())

   Shalloe Copy : Copy creates a new object

   list1 = [1,2,3] --> list1.append([5,6])

    list2 = copy.copy(list1)
    list1.append([5,6])

print(list1) [1,2,3,5,6]
print(list2) [1,2,3]

programiz

2. Deep Copy --> New object and adds

"""
x = 10
y = 10

if x is y:
    print("Neha")
else:
    print("kapoor")


""" .oor*?"""

