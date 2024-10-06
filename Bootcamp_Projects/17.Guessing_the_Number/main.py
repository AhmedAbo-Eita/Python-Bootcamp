# lGuessing the Number
# Instruction
# Create a program will generate a random number unknown to the user between upper and lower bond that user provided.
# The user needs to guess what that number is. If the user’s guess is wrong, the program should return some sort of
# indication as to how wrong (e.g. The number is too high or too low). If the user guesses correctly, a positive indication should appear.
#
# Your program should ask for upper and lower bound from the user initially.
#
# Calculate chances of user based on upper and lower bounds.
#
# Based on calculated number of chances ask input from user for guessing the number.
#
# If the guessed number is greater than the generated number then print - "You guessed too high", otherwise print -
# "You guessed too low". And finally if the numbers match print - "Congratulations you did it in"
#
# Output can be like this:
#
# Enter Lower bound: 1
# Enter Upper bound: 7
#     You've only  3  chances to guess the integer!
# Guess a number: 4
# You Guessed too high!
# Guess a number: 1
# You guessed too small!
# Guess a number: 2
# Congratulations you did it in  3  try
# The number is 2
#     Better Luck Next time!
# Hint
# Log function from math module to calculate chances. (math.log(upper - lower + 1, 2))


import random
import math
#asking user to enter the lower and upper bounds.
Lower_bound = int(input("Enter Lower bound: "))
Upper_bound = int(input("Enter Upper bound: "))

#set a random integer number for user
Guessing_Number = random.randint(Lower_bound,Upper_bound)

#let the user know that he has only 3 Guesses
trailers = math.ceil(math.log(Upper_bound-Lower_bound+1,2))
print(f"\n\tYou've only  {trailers}  chances to guess the integer!\n")

trail = 1
while trail <= trailers:
    User_input = int(input("Guess a number: "))
    if User_input < Guessing_Number:
        if trail == trailers:
            print(f"\nThe number is {Guessing_Number}\n\tBetter Luck Next time!")
        else:
            print("You Guessed too small!")
    elif User_input > Guessing_Number:
        if trail == trailers:
            print(f"\nThe number is {Guessing_Number}\n\tBetter Luck Next time!")
        else:
            print("You guessed too high!")
    elif User_input == Guessing_Number:
        print(f"Congratulations you did it in  {trail}  try")
        break
    trail += 1