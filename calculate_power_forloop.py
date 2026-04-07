# Python Program to calculate the power
# without using POW function.(using for loop).

base = int(input("Enter the value for base: "))
exponent = int(input("Enter the value for exponent: "))
result=1;
print(base,"to power ",exponent,"=",end = ' ')
#using ‘for’ loop with ‘range’ function
for exponent in range(exponent, 0, -1):
    result *= base
print(result)
