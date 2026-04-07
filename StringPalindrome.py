# Python program to check a String is palindrome or not.
# Using reverse and compare
string = input("Please give a String : ")
if(string == string[:: - 1]):
   print("Given String is a Palindrome")
else:
   print("Given String is not a Palindrome")

# Using method and for loop
def isPalindrome(string):
    for i in range(0, int(len(string)/2)):
        if string[i] != string[len(string)-i-1]:
            return False
    return True
string = input("Please give a String : ")
if (isPalindrome(string)):
    print("Given String is a Palindrome")
else:
    print("Given String is not a Palindrome")
