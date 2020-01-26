#Time Complexity O(N)
def check_permutation(str1, str2):
    set_str1, set_str2 = set(str1), set(str2) #Converts both input strings to sets
    return len(set_str1 ^ set_str2) == 0 #Uses XOR on the sets and checks to see if anything is duplicate

print(check_permutation("racecar","carrace")) #True
print(check_permutation("racecar","carraces")) # False
print(check_permutation("rammana","anagram")) #False
print(check_permutation("gramana","anagram")) #True
print(check_permutation(""," ")) #False

#No extra space, Time Complexity: O(n log n)
def check_permutation2(str1, str2):
    return sorted(str1) == sorted(str2) #Sorts strings, compares them


print(check_permutation2("racecar","carrace")) #True
print(check_permutation2("racecar","carraces")) # False
print(check_permutation2("rammana","anagram")) #False
print(check_permutation2("gramana","anagram")) #True
print(check_permutation2(""," ")) #False