# Python program to check given character is digit or not.
#taking input from user
ch = input("Enter a character : ")
if ch >= '0' and ch <= '9': #comparing the value of ‘ch’
	# if the condition holds true then this block will execute
    	print("Given Character ", ch, "is a Digit")
else: #this block will execute if the condition will not satisfies
    print("Given Character ", ch, "is not a Digit")