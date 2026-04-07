list1 = [1,2,3,4]
# use for loop and list comprehension
s1 = [x* x for x in list1]
print("Original list", list1)
print("Squared list",s1)

#using map() function and lambda function
s2 = list(map(lambda  x :x *x,list1))
print("Squared list using map(): ",s2)