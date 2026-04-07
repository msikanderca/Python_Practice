
# factorial program without using if-else, for, and ternary operators.

import math
def check_Fact(num):
    return (math.factorial(num))


num = int(input("Enter the number to find factorial:"))
fact = check_Fact(num)
print("Factorial of the number", num, "is", fact)
