# Python Program to Convert Decimal Number into Binary.
# Program 1: Convert Decimal to Binary Using Loop
decimal = temp = int(input("Please Enter a decimal number: "))
binary = ""
while temp > 0:
    remainder = temp % 2
    binary = str(remainder) + binary
    temp = temp // 2
print("Binary number is ", binary, " for ", decimal)

# Program 2: Decimal to Binary Using bin() function
decimal1 = int(input("Please Enter a decimal number: "))
binary1 = bin(decimal1)
print("Binary number is ", binary1[2:], " for ", decimal1)
