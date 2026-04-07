# Python program to insert an element at end of an Array.
# 1). Using append() Method
arr = [1,2,3,4,5]
num=int(input("Enter a number to insert in array at end :"))
# adding element at the end of the array(list)
arr.append(num)
print("Array after inserting",num,"at end",arr)


# 2). Using the insert() Method
arr1 = [1,2,3,4,5]
num1=int(input("Enter a number to insert in array at end :"))
# adding element at the end of the array(list)
arr1.insert(len(arr1), num1)
print("Array after inserting",num1,"at end",arr1)


# 3). Using the + Operator
arr1 = [1,2,3,4,5]
num1=int(input("Enter a number to insert in array at end :"))
# adding element at the end of the array(list)
arr1 += [num1]
print("Array after inserting",num1,"at end",arr1)