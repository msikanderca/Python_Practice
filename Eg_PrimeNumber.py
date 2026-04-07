# code to check prime numbers.
def is_prime_while(num):
    if num <= 1:
        return False
    i = 2
    while i <= int(num**0.5):
        if num % i == 0:
            return False
        i += 1
    return True
number = int(input("Enter a number: "))
if is_prime_while(number):
    print(f"{number} is a prime number.")
else:
    print(f"{number} is not a prime number.")
