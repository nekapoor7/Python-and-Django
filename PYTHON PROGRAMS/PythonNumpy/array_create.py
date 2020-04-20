import numpy as np

arr = np.array([1,2,3])

print(arr)

arr1 = np.array([[1,2,3],
                [4,5,6],
                [7,8,9]])
print(arr1)

arr = np.array([[-1, 2, 0, 4],
                [4, -0.5, 6, 0],
                [2.6, 0, 7, 8],
                [3, -7, 4, 2.0]])
print("Initial Array: ")
print(arr)

# Printing a range of Array
# with the use of slicing method
sliced_array = arr[:2, ::2]
print("Sliced Array \n",sliced_array)

# Printing elements at
# specific Indices
Index_arr = arr[[1, 1, 0, 3],
                [3, 2, 1, 0]]
print ("\nElements at indices (1, 3), "
    "(1, 2), (0, 1), (3, 0):\n", Index_arr)