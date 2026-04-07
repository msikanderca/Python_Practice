# Python program to print the highest frequency character in a String.
# Method 1: Using a Dictionary
string = input("Please Enter a string: ")
freq_dict = {}
# Count the frequency of each character
for char in string:
    if char in freq_dict:
        freq_dict[char] += 1
    else:
        freq_dict[char] = 1
max_freq = max(freq_dict.values())
# Print the characters with maximum frequency
for char in freq_dict:
    if freq_dict[char] == max_freq:
        print(char, end=' ')