# Python program to check given character is vowel or consonant.
ch = input("Enter a character to check if it's a vowel or consonant: ")

# Check if input is a single alphabet character
if len(ch) == 1 and ch.isalpha():
    if ch.lower() in ('a', 'e', 'i', 'o', 'u'):
        print("Given character", ch, "is a vowel")
    else:
        print("Given character", ch, "is a consonant")
else:
    print("Please enter a single alphabet character only.")