#palindrome
# Program to check if a string is palindrome or not

data = input ("Enter data: ")
data= data.casefold()  # case less comparison

# reverse the string

rev_str = reversed(data)

# check if the string is equal to its reverse

if list(data) == list(rev_str):
   print("The string is a palindrome.")
else:
   print("The string is not a palindrome.")
