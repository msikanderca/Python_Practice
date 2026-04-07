# Python program to print all non repeating character in string.
# Program 1: Using a Dictionary to Count Occurrences
string = input('Please enter a string: ')
freq_dict = {}
for char in string:
    if char in freq_dict:
        freq_dict[char] += 1
    else:
        freq_dict[char] = 1
non_repeating_chars = ""
for char in string:
    if freq_dict[char] == 1:
        non_repeating_chars += char
print("Non-repeating characters:", non_repeating_chars)

#Program 2: Using Collections.Counter
from collections import Counter
string1 = input('Please enter a string: ')
counts = Counter(string1)
non_repeating = [char1 for char1, count in counts.items() if count == 1]
print("non repeating characters = ", non_repeating)