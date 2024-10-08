# Rock, Paper, Scissors
# Instruction
# Create a program which simulates Rock, Paper, Scissors Game Steps:
#
# Ask user to select rock, paper or scissors
#
# Then generate computer selection by using random module
#
# Then determine winner based on computer selection and user selection
#
# Finally, ask whether they want to play again or not
#
# Sample Output:
#
# Enter a choice (rock, paper, scissors): paper
# You chose paper, computer chose scissors.
# Scissors cuts paper! You lose.
# Play again (Y/N)? Y
# Enter a choice (rock, paper, scissors): paper
# You chose paper, computer chose scissors.
# Scissors cuts paper! You lose.
# Play again (Y/N)? Y
# Enter a choice (rock, paper, scissors): rock
# You chose rock, computer chose paper.
# Paper covers rock! You lose.
# Play again (Y/N)?
# Hint
# Use choice() function from random module to select random elements from option list./

import random

options = ["rock", "paper", "scissors"]

#Game logic
def the_winner(p_user_choice,p_computer_choice):
    # in case of both user and computer choose the same thing
    if p_user_choice == p_computer_choice:
        print(f"Both players selected {p_user_choice}. It's a tie!")
    #in case of user choose rock
    elif p_user_choice=="rock":
        if p_computer_choice == "scissors":
            print("Rock smashes scissors! You win!")
        elif p_computer_choice=="paper":
            print("Paper covers rock! You lose.")
    #in case of user choose paper
    elif p_user_choice=="paper":
        if p_computer_choice == "scissors":
            print("Scissors cuts paper! You lose.")
        elif p_computer_choice=="rock":
            print("Paper covers rock! You win!")
    # in case of user choose paper
    elif p_user_choice == "scissors":
        if p_computer_choice == "paper":
            print("Scissors cuts paper! You win!.")
        elif p_computer_choice == "rock":
            print("Rock smashes scissors! You lose.")
    else:
        print("your input is invalid")


condition = 'y'
while condition == 'y' or condition == 'Y':
    # take input from user
    user_choice = input("Enter a choice (rock, paper, scissors): ")
    # convert the input to lower letters
    user_choice = str.lower(user_choice)
    computer_choice = random.choice(options)
    # print the result
    print(f"You chose {user_choice}, computer chose {computer_choice}.")

    #calling the function
    the_winner(user_choice,computer_choice)

    #dasking for continue
    condition = input("Play again (Y/N)? ")