# Count Characters in a String
# Implement a function count_letter that takes two parameters : a string and a letter, 
# then returns the  number of times the letter  appears in a string

# Example:
# count_letter("Learning Python", "n")
# Output
# 3

def count_letter(word, letter):
    # count is a variable save the number of letters in word
    count = 0
    for character in word:
        if letter == character:
            count += 1
    return count

#take inputs from user
user_word = input("Enter the word: ")
user_letter = input("Enter the letter: ")

#calling function cont letters 
result = count_letter(user_word,user_letter)

#print the result 
print(result)
