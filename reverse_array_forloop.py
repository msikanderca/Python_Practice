# Python program to reverse an Array in two ways.


# Taking the input from the user to fix the array size
size = int(input("Enter the number of elements you want in array: "))

# Creating an empty list
arr = []

# Adding the elements of the list by taking inputs from the user
for i in range(0, size):
    elem = int(input("Please give value for index " + str(i) + ": "))
    arr.append(elem)

print("Array in reverse order:")

# Reversing the list and printing it
for i in range(size - 1, -1, -1):
    print(arr[i], end=' ')
