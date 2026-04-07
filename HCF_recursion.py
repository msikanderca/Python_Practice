
# Python Program to find GCD of two numbers using recursion.


def gcd(num1,num2):
    if num2 == 0:
        return num1;
    return gcd(num2, num1 % num2)
#taking inputs from the user
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
print("hcf/gcd of",num1,"and",num2,"=",gcd(num1,num2))