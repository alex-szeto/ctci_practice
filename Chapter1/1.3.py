#Time Complexity O(N)
def URLify(input):
    return input.replace(" ", "%20") #Using built in replace function

print(URLify("Mr John Smith")) # => Mr%20John%20Smith
print(URLify("NoSpaces")) # => NoSpaces

def URLify2(input): #Without using replace function
    char_list = input.split(" ") #splits at spaces
    return "%20".join(char_list) #joins with %20

print(URLify2("Mr John Smith")) # => Mr%20John%20Smith
print(URLify2("NoSpaces")) # => NoSpaces



