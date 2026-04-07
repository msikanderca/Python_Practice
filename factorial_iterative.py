# Python Program to calculate factorial using iterative method.
num = int(input("Enter the whole number to find the factorial: "))
factorial = 1

if num < 0:
    print("Factorial can't be calculated for negative numbers.")
elif num == 0:
    print("Factorial of 0 is 1")
else:
    # calculating the factorial of the input number
    for i in range(1, num + 1):
        factorial *= i
    print(f"Factorial of {num} is {factorial}")