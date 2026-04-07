# Get input from the user
original_string = input("Enter a string: ")
# Reverse the string using slicing
reversed_string = original_string[::-1]
# Print the reversed string
print("Reversed string:", reversed_string)


if original_string == reversed_string:
    print ("palindrome")
else:
    print ("not")