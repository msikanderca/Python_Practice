# Python program to count the Occurrence Of Vowels & Consonants in a String.
string = input("Enter a String : ")
vowels = 0
consonants = 0
for i in string:  #string iteration
    if i in ('a', 'e', 'i', 'o', 'u','A', 'E', 'I', 'O', 'U'):
        vowels+=1
    elif i.isalpha():
        consonants+=1
print("Vowels :",vowels,"Consonants:",consonants)

# Program 2: Using Python Collections – Counter
from collections import Counter
string1 = input("Enter a String: ")
vowel_set = set('aeiouAEIOU')  #A set of vowels,both uppercase and lowercase
count1 = Counter(string)
vowel_count = sum(count1[char] for char in count1 if char in vowel_set)
consonant_count = sum(count1[char] for char in count1
                      if char.isalpha() and char not in vowel_set)
print("Vowels:", vowel_count, "Consonants:", consonant_count)

# Program 3: Using filter and Lambda
string2 = input("Enter a String: ")
vowels2 = 'aeiouAEIOU'
is_vowel = lambda x: x in vowels2
is_consonant = lambda x: x.isalpha() and x not in vowels2
vowel_count2 = len(list(filter(is_vowel, string2)))
consonant_count2 = len(list(filter(is_consonant, string2)))
print(f"Vowels: {vowel_count2}, Consonants: {consonant_count2}")