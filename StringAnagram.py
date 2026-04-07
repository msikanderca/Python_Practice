# Python Program to check if two Strings are Anagram.
# Program 1: Basic Anagram Check Using Sorting
def anagram_check(str1, str2):
    if len(str1) != len(str2):
            return False
    if (sorted(str1) == sorted(str2)) :
	    return True
    else :
	    return False
str1 = input("Please enter String 1 : ")
str2 = input("Please enter String 2 : ")
if anagram_check(str1,str2):
    print("Anagram")
else:
    print("Not an anagram")

# Program 2: Anagram Check by Counting Characters
from collections import Counter
def is_anagrams(str11, str21):
    return Counter(str11) == Counter(str21)
# Example usage:
print(is_anagrams("tide", "diet"))
print(is_anagrams("hello", "python"))

# Program 3: Finding All Anagrams from a List
def check_anagrams(word, candidates):
    sorted_word = sorted(word)
    return [w for w in candidates if sorted(w) == sorted_word]
string_list = ["tide", "google", "deit", "hcl"]
print(check_anagrams("tied", string_list))

# Program 4: Grouping Anagrams
from collections import defaultdict
def anagrams_grouping(words1):
    anagram_map = defaultdict(list)
    for word1 in words1:
        key = tuple(sorted(word1))
        anagram_map[key].append(word1)
    return list(anagram_map.values())
string_list1 = ["tied", "hello", "diet", "act", "ohlel", "cta"]
print(anagrams_grouping(string_list1))