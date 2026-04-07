# code to check prime numbers.
num = int(input("Enter a number: "))
temp = 0
for i in range (2, int (num/ 2) ):
    if num % i == 0 :
        temp += 1
if temp == 0:
    print ("Prime")
else:
    print ("not")
