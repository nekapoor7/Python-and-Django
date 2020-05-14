"""Write a Python program to sort Counter by value. Go to the editor
Sample data : {'Math':81, 'Physics':83, 'Chemistry':87}
Expected data: [('Chemistry', 87), ('Physics', 83), ('Math', 81)]"""

from collections import OrderedDict
from operator import itemgetter
d = {'Math':81, 'Physics':83, 'Chemistry':87}

dd = OrderedDict(sorted(d.items(),key=itemgetter(1),reverse=True))
print(dd)