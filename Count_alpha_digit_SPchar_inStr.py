# Python program to count alphabets, digits and special characters.
# Program 1: Using isalpha() and isdigit() method
string = input("Enter a String : ")
alphabets=0
digits=0
specialChars=0
#checks for each character in the string
for i in string:
	#if character of the string is an alphabet
    		if i.isalpha():
       			 alphabets+=1
		#if character of the string is a digit
    		elif i.isdigit():
        			digits+=1
    		else: #if character of the string is a special character
        			specialChars+=1
print("alphabets =",alphabets,"digits =",digits,"specialChars =",specialChars)

# Program 2: Using Regular Expressions
import re
string = input("Enter a String : ")
alphabets = len(re.findall(r'[a-zA-Z]', string))
digits = len(re.findall(r'\d', string))
specialChars = len(re.findall(r'\W', string))
print("alphabets =",alphabets,"digits =",digits,"specialChars =",specialChars)

# Program 3: Using Collections.Counter
from collections import Counter
input_string = input("Enter a String : ")
count = Counter(input_string)
alphabets = sum(count[char] for char in count if char.isalpha())
digits = sum(count[char] for char in count if char.isdigit())
specialChars = sum(count[char] for char in count if not char.isalnum() and not char.isspace())
print("alphabets =",alphabets,"digits =",digits,"specialChars =",specialChars)