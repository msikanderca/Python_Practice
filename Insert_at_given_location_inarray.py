# Python program to insert element at a given location in Array.
# Program 1: Using the insert() Method
# given array (list)
arr = [1, 2, 3, 4, 5]
num=int(input("Enter a number to insert in array : "))
index=int(input("Enter a index to insert value : "))
if index >= len(arr):
    print("please enter index smaller than",len(arr))
else:
    # insering element ‘num’ at ‘index’ position
    arr.insert(index, num)
print("Array after inserting",num,"=",arr)

# Program 2: Using Slicing
arr1 = [1, 2, 3, 4, 5]
num1=int(input("Enter a number to insert in array : "))
index1=int(input("Enter a index to insert value : "))
new_arrays1 = arr1[:index] + [num1] + arr1[index:]
print("Array after inserting",num1,"=",new_arrays1)