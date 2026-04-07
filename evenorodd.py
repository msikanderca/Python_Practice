# Python Program to check a given number is even or odd.
# Program 1: Basic Modulus Operator

num = int(input("Enter a number to check even/odd: "))
#if number is divisible by 2
if num%2 == 0:
   print(num,"is even number")
else:
   print(num,"is odd number")

# Program 2: Using Bitwise Operator
number = int(input("Enter a number to check if it is even or odd: "))
result = "Even" if (number & 1) == 0 else "Odd"
print(f"The number {number} is {result}.")

# Program 3: Using Lambda Function
check_even_odd = lambda num1: "Even" if num1 % 2 == 0 else "Odd"
number1 = int(input("Enter a number to check even/odd: "))
result1 = check_even_odd(number1)
print(f"The number {number1} is {result1}.")

# Program 4: Using Integer Division
def check_even_odd(num2):
    return "Even" if (num2 // 2) * 2 == num2 else "Odd"

number2 = int(input("Enter a number to check if it is even or odd: "))
result2 = check_even_odd(number2)
print(f"The number {number2} is {result2}.")