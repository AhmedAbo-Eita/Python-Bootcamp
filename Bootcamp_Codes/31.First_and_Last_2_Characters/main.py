# First and Last 2 Characters
# Implement a function which takes a string as a parameter and returns new string which is made of the first 2 and the last
#  2 chars from a given a string. If the length of given string is less than 2 then return empty string.

# Example
# first_last_characters('appmillers')
# Output
# aprs

def first_last_characters(word):
    if len(word)<2:
        return ""
    else:
        result = word[0]+word[1]+word[-2]+word[-1]
        return result

#take input from user
user_word = input("Enter your word: ")

#calling the function 
out = first_last_characters(user_word)

#print the result
print(out)