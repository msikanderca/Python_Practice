#code to swap two variables.

# traditional method using temp variable:
num1 = input('Enter the first variable: ')
num2 = input('Enter the second variable: ')

#Printing the numbers before swap
print('The value of num1 before swapping: {}'.format(num1))
print('The value of num2 before swapping: {}'.format(num2))

#Use temporary variable and swap the values
temp = num1
num1 = num2
num2 = temp

#Printing the numbers after swap
print('The value of num1 after swapping: {}'.format(num1))
print('The value of num2 after swapping: {}'.format(num2))

# method used to swap,specific to pyhon :
num3 = input('Enter the third variable: ')
num4 = input('Enter the fourth variable: ')

#Printing the numbers before swap
print('The value of num3 before swapping: {}'.format(num3))
print('The value of num4 before swapping: {}'.format(num4))

num3 , num4 = num4, num3  # swapping variables using tuple unpacking

print('The value of num3 after swapping: {}'.format(num3))
print('The value of num4 after swapping: {}'.format(num4))