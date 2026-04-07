# Python Program to delete given element from Array.
# Program 1: Using the remove() Method
size=int(input("Enter the number of elements you want in array: "))
arr=[]
for i in range(0,size):
    elem=int(input("Please give value for index "+str(i)+": "))
    arr.append(elem)
num=int(input("Enter a number to remove from array : "))
arr.remove(num)
print("Array after removing",num,"=",arr)

# Program 2: Using List Comprehension
size1 = int(input("Enter the number of elements you want in the array: "))
arr1 = []
for i1 in range(size1):
    elem1 = int(input(f"Please give value for index {i1}: "))
    arr1.append(elem1)
num1 = int(input("Enter a number to remove from the array: "))
new_numbers1 = [x for x in arr1 if x != num1]
print("Array after removing:", new_numbers1)