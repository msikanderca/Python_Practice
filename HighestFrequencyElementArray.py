# Python Program to find highest frequency element in array.

# Program: Using a dictionary
arr = [1, 2, 3, 4, 5, 6, 5, 4, 5, 1, 2, 3, 4, 5, 6, 5, 4, 5]
freq_dict = {}
for element in arr:
    if element in freq_dict:
        freq_dict[element] += 1
    else:
        freq_dict[element] = 1
highest_freq_element = max(freq_dict, key=freq_dict.get)
print("Highest frequency element:", highest_freq_element)