# Write a program in Python to find second highest number in an integer array.
arr = []
n = int(input("Enter size of array: "))
for _ in range(n):
    val = int(input("Enter element of array: "))
    arr.append(val)

# Remove duplicates and sort in ascending order
unique_sorted = sorted(set(arr))

if len(unique_sorted) < 2:
    print("Second largest element does not exist.")
else:
    print(f"Second largest element is {unique_sorted[-2]}")