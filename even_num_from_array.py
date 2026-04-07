# Python Program to print all even numbers in array.
#taking the input from the user to fix the array size
size=int(input("Enter the number of elements you want in array: "))
arr=[]
# adding elements to the array (list)
for i in range(0,size):
    elem=int(input("Please give value for index "+str(i)+": "))
    arr.append(elem)
print("All even number in array are ")
# check and print if any element of array (list) is even
for i in range(0,size):
    if arr[i]%2==0:
        print(arr[i],end=' ')