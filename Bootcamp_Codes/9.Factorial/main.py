# Write a program that calculates the factorial (!) of any given number by a user.
# 3! = 3*2*1 = 6
# 4! = 4*3*2*1 = 24

# Example Input
# Enter a number: 4
# Example Output
# The factorial of 4 is: 24

import math

num = int(input("Enter a number: "))
factorial = math.factorial(num)
print(f"The factorial of {num} is: {factorial}")