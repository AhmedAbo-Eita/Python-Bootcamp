# Dice Rolling
# Instruction
# When the program runs, it will randomly choose a number between 1 and 6. Then program will print what that number is. It should then ask you if you’d like to roll again.
#
# Output
# Dice1: 3
# Dice2: 6
# Roll the dice again? (Y/N)

import random



def roll_dice():
    num1 = random.randint(1,6)
    num2 = random.randint(1,6)
    print(f"Dice1: {num1}")
    print(f"Dice1: {num2}")

while True:
    roll_dice()
    user_input = input("Roll the dice again? (Y/N)    ")
    if  user_input == 'N' or user_input == 'n':
        break
    elif user_input == 'Y' or user_input == 'y':
        continue
    else:
        print("You must enter Y/N")
        break
