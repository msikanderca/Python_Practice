# Python Program to sort character of string in descending order.

string = input("Enter the string : ")
#converting string into list of its characters
strList=list(string)
#sorting elements of list in reverse order by making ‘reverse = True’
sortedString=''.join(sorted(strList, reverse =True))
print("String Sorted in ascending order :", sortedString)