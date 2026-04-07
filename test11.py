



def pal(n):
    return n == n[::-1]
n = str(input ("Enter number:"))

if pal (n):
    print("Palindrome")
else:
    print("not palindrome")