"""Python | Merging two Dictionaries"""

dict1 = {'ravi':'10','rajnish':'9','sanjeev':'15','yash':'2','suraj':'32','neha':'7','harsh':'25'}

dict2 = {'rajnish': '9', 'sanjeev': '15', 'yash': '2', 'harry': '32'}

dict3 = {}

dict3 = {**dict1,**dict2}

print(dict3)