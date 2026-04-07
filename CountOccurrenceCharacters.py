# Python Program to count occurrence of a given characters in string.
# Program 1: Using for Loop
string = input("Please enter String : ")
char = input("Please enter a Character : ")
count = 0
for i in range(len(string)):
    if(string[i] == char):
        count = count + 1
print("Total Number of occurence of ", char, "is :" , count)

# Program 2: Using while Loop
string1 = input("Please enter String : ")
char1 = input("Please enter a Character : ")
index, count1 = 0, 0
while(index < len(string1)):
    if(string1[index] == char1):
        count1 = count1 + 1
    index = index + 1
print("Total Number of occurence of ", char1, "is :" , count1)

#Program 3: Using Method
def countOccur(char2, string2):
    count2 = 0
    for i in range(len(string2)):
        if(string2[i] == char2):
            count2 = count2 + 1
    return count2
string2 = input("Please enter String : ")
char2 = input("Please enter a Character : ")
count2 = countOccur(char2, string2)
print("Total Number of occurence of ", char2, "is :" , count2)