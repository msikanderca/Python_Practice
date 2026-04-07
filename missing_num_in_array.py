# Write a program in Python for, In array 1-100 numbers are stored, one number is missing how do you find it.
# Program 1: Using the Formula for the Sum

# Initialize the array
arr = [1, 2, 3, 5]
# Calculate the total number of elements expected (including the missing one)
n = len(arr) + 1
# Calculate the sum of the first n natural numbers
total_sum = (n * (n + 1)) // 2  # Use integer division for safety
# Calculate the sum of the elements in the array
sumArr = sum(arr)
# Calculate the missing number
missing_number = total_sum - sumArr
# Print the missing number
print("Missing number =", missing_number)

# Program 2: Using Sorting
def get_missing_number1(arr1):
    arr1.sort()
    for i in range(len(arr1)):
        if arr1[i] != i + 1:
            return i + 1
    return len(arr1) + 1
array1 = [1, 2, 3, 4]
print("Missing number =", get_missing_number1(array1))

#Program 3: Using Set for Direct Lookup
array2 = [1, 2, 3, 4]
num_set2 = set(array2)
n = len(array2) + 1
missing_number2 = None
for number2 in range(1, n + 1):
    if number2 not in num_set2:
        missing_number2 = number2
        break
if missing_number2 is not None:
    print("Missing number =", missing_number2)
else:
    print("No missing number, the sequence is complete.")
