my_list = [10, 20, 30, 40, 50]
del my_list[2]  # Deletes the element at index 2 (value 30)
print(my_list)  # Output: [10, 20, 40, 50]
del my_list[1:3]  # Deletes elements from index 1 to 2 (values 20 and 40)
print(my_list)  # Output: [10, 50]
#del my_list  # Deletes the entire list
# print(my_list)  # This would raise a NameError because the list no longer exists
my_list1= [10, 20, 30, 40, 50]
list_length = len(my_list1)
print(list_length)  # Output: 5
print(my_list1)  # Output: [10, 20, 30, 40, 50] - The list remains unchanged
print (my_list1 [-2])
my_list1.append(80)
print(my_list1)
rev = [val ** 2 for val in my_list1]
print (rev)





