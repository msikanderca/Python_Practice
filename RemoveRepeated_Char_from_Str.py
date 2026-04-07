# Python program to remove repeated character from string.
# Method 1: Using a Set and String Concatenation
def remove_duplicates(s):
    unique_chars = set()
    output = ""
    for char in s:
        if char not in unique_chars:
            unique_chars.add(char)
            output += char
    return output
string = input("Please Enter a string: ")
print(remove_duplicates(string))

# Method 2: Using a List and Join
def remove_duplicates1(s1):
    unique_chars1 = []
    for char1 in s1:
        if char1 not in unique_chars1:
            unique_chars1.append(char1)
    return "".join(unique_chars1)
string1 = input("Please Enter a string: ")
print(remove_duplicates(string1))