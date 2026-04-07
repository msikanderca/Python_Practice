num1 = input('Enter the first number: ')
num2 = input('Enter the second number: ')

# Converting and adding two numbers using int() & float() functions
sum = int(num1) + int(num2)

# Subtracting the two numbers  
sub = int(num1) - int(num2)  

# Multiplying two numbers  
mul = float(num1) * float(num2)  

#Dividing two numbers  
div = float(num1) / float(num2) 

# Displaying the results of arithmetic operations
print('The sum of {0} and {1} is {2}'.format(num1, num2, sum))
print('The subtration of {0} and {1} is {2}'.format(num1, num2, sub))
print('The multiplication of {0} and {1} is {2}'.format(num1, num2, mul))  
print('The division of {0} and {1} is {2}'.format(num1, num2, div))