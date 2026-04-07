# Write a program in Python to find largest and smallest number in array.
arr = []
n = int(input("Enter the size of the array: "))
# Taking array input from user
for _ in range(n):
    element = int(input("Enter an element of the array: "))
    arr.append(element)
# Initializing largest and smallest with the first element
largest = arr[0]
smallest = arr[0]

# Finding largest and smallest
for num in arr:
    if num > largest:
        largest = num
    if num < smallest:
        smallest = num
# Displaying the result
print(f"Largest element in the array is {largest}")
print(f"Smallest element in the array is {smallest}")