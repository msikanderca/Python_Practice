# Python program to replace the string space with a given character.
string = input("Enter a string: ")
ch = input("Enter a character to replace spaces: ")

result = ''  # Empty string to store the result

# Iterating using a for loop
for i in string:
    if i == ' ':      # If space is found
        i = ch        # Replace it with the given character
    result += i       # Append the character to the result

# Printing the modified string
print("String after replacing spaces with", ch, "=", result)