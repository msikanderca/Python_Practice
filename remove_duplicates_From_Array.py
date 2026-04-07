# Write a program in Python to remove duplicate elements form array.
arr = []
n = int(input("Enter size of array: "))
for _ in range(n):
    val = int(input("Enter element of array: "))
    arr.append(val)

print("Array elements after removing duplicates:")

seen = set()
for val in arr:
    if val not in seen:
        print(val)
        seen.add(val)