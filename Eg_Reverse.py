# Get input from the user
original_string = input("Enter a string: ")
# Reverse the string using slicing
reversed_string = original_string[::-1]
# Print the reversed string
print("Reversed string:", reversed_string)


#get input from user
s1 =input("Enter a string: ")
s2 =""
for i in s1:
    s2 =i+s2
print("Original String: ", s1)
print("Reverse String: ", s2)