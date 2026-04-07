# factorial program without using if-else, for, and ternary operators.
import math
def check_Fact(num):
    return (math.factorial(num))
num = int(input("Enter the number to find factorial:"))
fact = check_Fact(num)
print("Factorial of the number", num, "is", fact)


# using functions
def fact(n1):
    f =1
    if n1<0:
        print ("sorry, factorial is not available to negative number")
    elif n1 ==0:
        print("Factorial of",n1, "is 1")
    else:
        for i in range (1, n1+1):
            f = f * i
        print("Factorial of",n1, "is",f)

fact(int (input("Enter the number to find factorial:")))

