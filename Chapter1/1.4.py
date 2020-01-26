
#Time Complexity O(n)
import re
def palindrome_permutation(input_string):
    frequency = {} #Dictionary to keep track of character occurrences
    stripped = re.sub("[^a-z]","",input_string.lower()) # Given that we can ignore cases and non-letter characters
    
    for c in stripped:
        frequency[c] = frequency.get(c, 0) + 1 #maps characters to their frequency

    middle = False #palindromes can only have one character frequency as odd, as a middle character

    for i in frequency.values(): #iterates through dictionary values
        if i % 2 == 1: #if the value is i % 2 == 1, it means the character is either the middle or it's not a valid palindrome. Because all palindromes must have an even number of characters aside from the middle
            if middle == True: #checks to see if there is already a middle
                return False #if so, it's not a palindrome
            middle = True #if not, set that a middle
    return True #if everything passes, return true
    
print(palindrome_permutation("this is not a palindrome")) #false
print(palindrome_permutation("tact coa")) #true