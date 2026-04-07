# append list with new item
number = [10,5,7,18,4,20,5,7,4]
number.append(8)
print (number)
# remove item from list -- this will remove first occurrence of item
number.remove(5)
print (number)
# insert the item at a specific location in list
number.insert(3,55)
print(number)
# remove last item from list
number.pop()
print(number)
# clear the list
number.clear()
print(number)
number1 = [33,44,22,66,55,77]
#check for existing item in list using index
print(number1.index(66))
#check for existing item in list using In operator
print(50 in number1)
print(22 in number1)
#check no. of occurrence of items in list
print(number1.count(77))
#sort in ascending order
number1.sort()
print(number1)
# reverse the list
number1.reverse()
print(number1)






