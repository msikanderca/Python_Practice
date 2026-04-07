# Program 1: Using the pop() method
arr = [1, 2, 3, 4, 5]
arr.pop(2)
print("Array after removing from index : ", arr)

# Program 2: Using the del keyword
arr1 = [1, 2, 3, 4, 5]
del arr1[2]
print("Array after removing from index : ", arr1)

# Program 3: Using Slicing Keyword
arr2 = [1, 2, 3, 4, 5]
arr2 = arr2[:2] + arr2[3:]
print("Array after removing from index : ", arr2)