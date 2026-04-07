# Write a program in Python for, In a array 1-100 multiple numbers are duplicates, how do you find it.
# Program 1: Using for Loop

arr, occur = [], []
n = int(input("please enter the size of array: "))
for x in range(n):
    occur.append(0)
for x in range(n):
    element = int(input(f"please enter the element of array element between 0 to {n-1} :"))
    arr.append(element)
    occur[arr[x]]=occur[arr[x]]+1
for x in range(n):
    if occur[x]>1:
        print(f"{x} is repeated {occur[x]} times")

# Program 2: Using a Set to Track Seen Elements
n1 = int(input("Please enter the size of the array: "))
arr1 = []
print("Please enter the numbers in the array:")
for i in range(n1):
    arr1.append(int(input()))
seen1 = set()
duplicates1 = []
for num1 in arr1:
    if num1 in seen1:
        duplicates1.append(num1)
    else:
        seen1.add(num1)
print("Duplicates:", duplicates1)

# Program 3: Using a Dictionary to Count Occurrences
n2 = int(input("Please enter the size of the array: "))
arr2 = []
print("Please enter the numbers in the array:")
for i in range(n2):
    arr2.append(int(input()))
counts2 = {}
duplicates2 = []
for num2 in arr2:
    if num2 in counts2:
        counts2[num2] += 1
    else:
        counts2[num2] = 1
for num2, count2 in counts2.items():
    if count2 > 1:
        duplicates2.append(num2)
print("Duplicates:", duplicates2)


# Program 4: Using List Comprehension and count()
n3 = int(input("Please enter the size of the array: "))
arr3 = []
print("Please enter the numbers in the array:")
for i in range(n3):
    arr3.append(int(input()))
duplicate_numbers3 = list({x for x in arr if arr3.count(x) > 1})
print("Duplicates:", duplicate_numbers3)