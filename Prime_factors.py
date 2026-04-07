#Write a program in Python to find prime factors of a given integer.
# Program 1: Using Trial Division
def prime_factors(n):
    i = 2
    factors = []
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            factors.append(i)
    if n > 1:
        factors.append(n)
    return factors
num = int(input("Please enter a number: "))
print("Prime factors of", num, "are:", prime_factors(num))
# Program 2: Optimized Trial Division Using 2 and Odd Numbers
num1 = int(input("Please enter a number: "))
n1 = num1
factors1 = []
while n1 % 2 == 0:
    factors1.append(2)
    n1 //= 2
factor1 = 3
while factor1 * factor1 <= n1:
    while n1 % factor1 == 0:
        factors1.append(factor1)
        n1 //= factor1
    factor1 += 2
if n1 > 1:
    factors1.append(n1)
print("Prime factors of", num1, "are:", factors1)