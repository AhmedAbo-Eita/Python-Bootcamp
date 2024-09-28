# Write a virtual coin toss program which will randomly tell the user "Heads" or "Tails".
# There are many ways of doing this. But here you should generate a random number, 
# either 0 or 1. Then based on that number we will print out Heads or Tails.
# 1 means Heads
# 0 means Tails

# Example Output
#     Heads
# or
#     Tails

import random

value = random.randint(0,1)

if value == 1:
    print("Heads")
else:
    print("Tails")