# Python Program to delete element at end of Array.
# Program 1: Using pop() function
arr = [1, 2, 3, 4, 5]
arr.pop()
print("Array after delete at end:", arr)

# Program 2: Using slicing
arr1 = [1, 2, 3, 4, 5]
#removing the last element using slicing
arr1 = arr1[:-1]
#printing the updated array
print("Array after delete at end:", arr1)

# Program 3: Using del keyword
arr2 = [1, 2, 3, 4, 5]
#removing the last element using del keyword
del arr2[-1]
#printing the updated array
print("Array after delete at end:", arr2)