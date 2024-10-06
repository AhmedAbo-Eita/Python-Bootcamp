# Instruction
# Create a program will generate a password based on user inputs. Initial variables are already provided.
#
# letters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
# nums = "1234567890"
# symbols = "-+=!@#$%^&*"
# Your program should ask for number of letters, symbols and numbers initially
#
# Then based on these inputed values it will generate password
#
# Output can be like this:
#
# How many letters do you want in your password? 8
# How many numbers do you want in your password? 2
# How many symbols do you want in your password? 2
# Your password is: EDUpEYIG67*@
# Hint
# Use choice() function from random module to select random character from letters, nums or symbols.

import random

letters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
nums = "1234567890"
symbols = "-+=!@#$%^&*"

num_letters = int(input("How many letters do you want in your password? "))
num_numbers = int(input("How many numbers do you want in your password? "))
num_symbols = int(input("How many symbols do you want in your password? "))

password = ""

for letter in range(0,num_letters):
    password += random.choice(letters)

for num in range(0,num_numbers):
    password += random.choice(nums)

for num in range(0,num_symbols):
    password += random.choice(symbols)

list_password = list(password)
random.shuffle(list_password)


advanced_password = ""

for counter in list_password:
    advanced_password += counter
print(f"Your Password is {password}")
print(f"Your advanced password is {advanced_password}")