#Python Program to Demonstrate Explicit Type Conversion

#Explicit type casting example
num1 = 123
num2 = "456"

print("Datatype of num1:",type(num1))
print("Datatype of num2 before Type Casting:",type(num2))

#Convertion of num2 from string(higher) to integer(lower) type using int() function to perform the addition between num1 and num2.

num2 = int(num2)
print("Datatype of num2 after Type Casting:",type(num2))

num3 = num1 + num2

print("Sum of num1 and num2:",num3)
print("Data type of the num3:",type(num3))