# Python Program to find sum of array elements.
# Program 1: Using + Arithmetic Operation
size=int(input("Enter the number of elements you want in array: "))
arr=[]
sum1=0
# adding elements to the array (list)
for i in range(0,size):
    elem=int(input("Please give value for index "+str(i)+": "))
    arr.append(elem)
    sum1+=elem
print("Sum of list elements = ",sum1)

# Program 2: Using the Built-in sum() Function
numbers1 = [1, 2, 3, 4, 5]
result1 = sum(numbers1)
print("Sum of list elements :", result1)

# Program 3: Using functools.reduce()
from functools import reduce
numbers2 = [1, 2, 3, 4, 5]
result2 = reduce(lambda x, y: x + y, numbers2)
print("Sum of list elements:", result2)