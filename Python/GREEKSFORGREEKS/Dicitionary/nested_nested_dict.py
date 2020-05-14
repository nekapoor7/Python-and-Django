d = {'first_level':
                    {'second_level':
                                     {'third_3': 0, 'third_2': 4, 'third_1': 1}}}

#First we must 'reach' the innermost dictionary. Let's start with second level:
d1 = {}

d1 = [v.items() for k , v in d.items()]
print(d1)

#As we need third level we add one more nesting:
d2 = {}
d2 = [j.items() for k , v in d.items() for i , j in v.items()]
print(d2)

#Now we reached level we want to sort. It's time to use built-in function sorted(). As we can see the elements are tuples
# where value we want to sort is on index 1 (second element). So we add sorting:
d3 = {}
d3 = [sorted(j.items() ,key=lambda x:x[1]) for k , v in d.items() for i , j in v.items()]
print(d3)

#We have sorted third level but this ain't nested dictionary what we had at the beginning.
# So let's add second level back and turn to dictionary comprehension:
d4 = {}
d4 = {i : dict(sorted(j.items() ,key=lambda x:x[1])) for k , v in d.items() for i , j in v.items()}
print(d4)

#Lets add first level as well:
d5 = {}
d5 = {k : {i: dict(sorted(j.items() ,key=lambda x:x[1]))} for k , v in d.items() for i , j in v.items()}
print(d5)

#We have constructed new dictionary where third level dictionary is insertion sorted based on values.
# If we want reverse order then we just add reverse=True:

d6 = {}
d6 = {k : {i: dict(sorted(j.items() ,key=lambda x:x[1],reverse=True))} for k , v in d.items() for i , j in v.items()}
print(d6)

