#To add new elements in the list:
students = ['alice','bob','charlie','darwin','elsa']
print (students)
# print Bob
print (students[1])
 # print darwin
print (students[3])
# add john in the list
students.append ('john')
print (students)
# to add Kattie at 2nd index position
students.insert (2,'kattie')
print (students)
#To modify bob name and replace with Sam in the list:
students [1]  = 'sam'
print (students)
#To delete charlie name from the list:
del (students[3])
print (students)
# last element of the list:
print(students[-1])
# delete element from list
students.remove('sam')
print(students)
# delete using pop and indexing
students.pop(4)
print(students)
# delete entire list
students.clear()
print(students)