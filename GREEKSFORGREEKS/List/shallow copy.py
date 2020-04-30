""" Python Program to demonstarte Shallow Copy"""

""" A shallow Copy actually created a new object which stores the reference of the original elements and so a shallow copy
  doesn't create a copy of nested objects instead it just copies the reference of the nested objects 
  that means a copy process doesn't not recurs or create copy of the nested objects itself."""

""" A Deep copy creates a new object and recursively adds the copies of the nested objects present in the original elements"""

import copy

list1 = [[1,2,3],[4,5,6],[7,8,9]]