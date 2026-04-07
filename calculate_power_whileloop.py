# Python Program to calculate the power
# without using POW function.(using while loop).

base = int(input("Enter the value for base: "))
exponent = int(input("Enter the value for exponent: "))
result=1;
print(base," to power ",exponent,"=",end = ' ')
#using while loop with a condition that come out of while loop if exponent is 0
while exponent != 0:
    result = base * result
    exponent-=1
print(result)
