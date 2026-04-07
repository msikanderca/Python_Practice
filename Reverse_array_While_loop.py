# taking the input from the user to fix the array size
size=int(input("Enter the number of elements you want in array: "))
# Create two empty lists
arr=[]
revArr=[]
# adding the elements to the list
for i in range(0,size):
    elem=int(input("Please give value for index "+str(i)+": "))
    arr.append(elem)
startIndex = 0;
lastIndex = size - 1;
# iterate the while loop till the lastindex 0
while (lastIndex>=0):
    revArr.append(arr[lastIndex])
    startIndex+=1
    lastIndex-=1
# printing the reversed list
print("Array in reverse order")
for i in range(0,size):
    print(revArr[i],end=' ')