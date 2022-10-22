# function to check anagram
def anagramCheck(str1, str2):

    # converting each string to list and 
    # sorting using iteration
    x = [ string1[i] for i in range(0, len(str1))
        ]
    x.sort()

    y = [ string2[i] for i in range(0, len(str2))
        ]
    y.sort()

    # condition for anagram
    if (x==y):
        print("Strings are anagram.")
    else:
        print("Strings are not anagram.")

# driver code 
if __name__ == "__main__":

    # taking input of both strings
    string1 = input("Enter first string: ")
    string2 = input("Enter second string: ")

    # function call
    anagramCheck(string1, string2)



# another method of checking anagram 
# using sorted() method
'''
def anagramCheck(str1, str2):
    if (sorted(str1) == sorted(str2)):
        print("Strings are anagram")
    else:
        print("Strings are not anagram")

if __name__ == "__main__":
    string1 = input("Enter first string: ")
    string2 = input("Enter second string: ")

    anagramCheck(string1, string2)
'''
