# Python program to perform left rotation of array elements by two positions.

# Program 1: Using pop() and append()
arr = [1, 2, 3, 4, 5]
arr.append(arr.pop(0))
arr.append(arr.pop(0))
print("After two left rotation :",arr)

# Program 2: Using Slicing in Python
arr1 = [1, 2, 3, 4, 5]
arr1 = arr1[2:] + arr1[:2]
print("After two left rotaion :",arr1)

# Program 3: Using the For loop in Python

arr2 = [1, 2, 3, 4, 5]
for i in range(2):
    temp = arr2[0]
    for j in range(len(arr2)-1):
        arr2[j] = arr2[j+1]
    arr2[-1] = temp
print("After two left rotaion :",arr2)