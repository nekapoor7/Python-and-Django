import numpy as np

arr = np.array([[1,2,3],
               [4,5,6],
               [7,8,9]])

arr1 = np.array([[10,4,5],
                 [11,2,3],
                 [4,5,6]])

print("Addition",arr + arr1)

print("Subtraction",arr - arr1)

print("Multiplication",arr * arr1)

print("Division", arr / arr1)

print("Floor", arr // arr1)

print("\nAddition of Array elements: ",np.sum(arr))

print("Addition of Two Arrays:",np.add(arr,arr1))

print("Subtraction of Two Arrays:",np.subtract(arr,arr1))

print("Multiply of Two Arrays:",np.multiply(arr,arr1))

print("Division of Two Arrays:",np.divide(arr,arr1))

print("transpose of Array",arr.transpose())

print("Square Root of Array",np.sqrt(arr))

print(arr.shape)

print(type(arr))

print(arr.size)

print(arr.ndim)