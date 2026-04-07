# Python program to convert lowercase vowel to uppercase in string.
string = input("Enter a string: ")
# define lowercase vowels
vowels = "aeiou"
for char in string:
    if char in vowels:
        # convert the lowercase vowel to uppercase
        upper_char = char.upper()
        # replace the lowercase vowel with the uppercase vowel
        string = string.replace(char, upper_char)
print("Updated string:", string)