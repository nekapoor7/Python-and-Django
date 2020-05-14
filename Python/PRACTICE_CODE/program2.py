"""Python Program to Concatenate Two Dictionaries Into One"""


dict1 = {'ravi':'10','rajnish':'9','sanjeev':'15','yash':'2','suraj':'32','neha':'7','harsh':'25'}

dict2 = {'rajnish': '9', 'sanjeev': '15', 'yash': '2', 'harry': '32'}

concat = {**dict1,**dict2}

print(concat)
