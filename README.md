# Check_anagram
This repository detects if given strings are anagram or not.

# What is Anagram?
An Anagram is a condition where one string or number is rearranged in that manner; each character of the rearranged string or number must be a part of another string or number. For example -The python and yphton are anagrams; Java and avaJs are not.

# Code explanation
In the code, we have declared the anagramCheck() method, which takes two strings as an argument. These strings are converted into a list to sort. After sorting it will check whether all the characters in string 1 is included in string 2 and no extra characters included. If the condition satisfies, it will print 'The strings are anagram' otherwise 'not anagram'. 
The second method of checking anagram is using sorted(). Sorted() is a Python inbuilt function which does not modify the original string, but returns sorted string.
