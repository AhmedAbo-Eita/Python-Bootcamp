# Bill Roulette
# Instruction
#
# Create a program which which asks for names and select random name from the list of names. The person selected will have to pay for everybody's food bill.
# Example Input
#
# Elshad, Edy, Redy, John, Jenny
#
# Example Output
#
# Edy is going to pay for the meal today!
#



#using random to select a random person
import random

#take input from user the contains the names
user_input = input("Enter the names separated by comma ',': ")

#convert string to list
names_list = user_input.split(',')

#choose person from list of names
name = random.choice(names_list)

#print the result
print(f"{name} is going to pay for the meal today!")
