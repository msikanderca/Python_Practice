


#code to swap two variables.
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

