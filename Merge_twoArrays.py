# Python Program to merge two arrays.

# Program 1: Using the + operator
arr1 = [1, 2, 3]
arr2 = [4, 5, 6]
merged_arr = arr1 + arr2
print("Array After Merging =",merged_arr)


# Program 2: Using the append() method and a for loop
arr3 = [1, 2, 3]
arr4 = [4, 5, 6]
for element in arr4:
    arr3.append(element)
print("Array After Merging =",arr3)

# Program 3: Using the extend() method and a for loop
arr5 = [1, 2, 3]
arr6 = [4, 5, 6]
arr5.extend(arr6)
print("Array After Merging =",arr5)