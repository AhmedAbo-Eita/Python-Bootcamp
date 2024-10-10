# Sum of Digits
# Write a program which asks for any given integer number from the console and prints out the sum of digits of given number.

# Input
# Enter an integer number: 134
# Output
# 8

# Take input from user 
num = int(input("Enter an integer number: "))
sum = 0 

# calculating the sum of digits 
while num != 0:
    sum = sum + (num%10)
    num = num // 10 

print(sum)