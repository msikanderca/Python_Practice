# Python Program to find the Average of numbers with explanations.
# Program 1: Using a Simple Loop and Input from the User

size=int(input("Give the number of elements you want in array: "))
arr=[]
#taking input of the list
for i in range(0,size):
    elem=int(input("Enter the number "+str(i +1)+": "))
    arr.append(elem)
#taking average of the elements of the list
avg=sum(arr)/size
print("Average of the array elements is ",avg)


# Program 2: Using the Built-in sum() and len() Functions
def calculate_average(numbers):
    return sum(numbers) / len(numbers)
numbers = [10, 20, 30, 40, 50]
print("Average of the number is :", calculate_average(numbers))