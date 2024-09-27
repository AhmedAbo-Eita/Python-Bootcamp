# Instructions
# Write a program to test the compatibility between two people.
# Take both people's names and check for the number of times the letters in the word TRUE occurs. 
# Then check for the number of times the letters in the word LOVE occurs. Then combine these numbers to make a 2 digit number.
# For Love Scores less than 10 or greater than 85, the message should be:
# "Your score is **x**, you go together like coke and mentos."
# For Love Scores between 40 and 70, the message should be:
# "Your score is **y**, you are alright together."
# Otherwise, the message will just be their score. e.g.:
# "Your score is **z**."

# Example
# name1 = "David"
# name2 = "Jennifer"

# T occurs 0 times
# R occurs 1 time
# U occurs 0 times
# E occurs 2 times
# Total = 3
# L occurs 0 time
# O occurs 0 times
# V occurs 1 times
# E occurs 2 times
# Total = 3
# Love Score = 33
# Print: "Your score is 33."

# Example Input 1
# name1 = "David"
# name2 = "Jennifer"
# Example Output 1
# Your score is 33.

# Hint
# The lower() function changes all the letters in a string to lower case.
# The count() function will give you the number of times a letter occurs in a string.

name1 = input("Enter Your Name: ")
name2 = input("Enter Your Lover Name: ")

name1 = name1.lower()
name2 = name2.lower()

t = name1.count('t')+name2.count('t')
r = name1.count('r')+name2.count('r')
u = name1.count('u')+name2.count('u')
e = name1.count('e')+name2.count('e')
l = name1.count('l')+name2.count('l')
o = name1.count('o')+name2.count('o')
v = name1.count('v')+name2.count('v')

score = int(str(t+r+u+e)+str(l+o+v+e))

if score<10 or score>85:
    print(f"Your score is {score}, you go together like coke and mentos.")
elif score>=40 and score<=70:
    print(f"Your score is {score}, you are alright together.")
else:
    print(f"Your score is {score}.")