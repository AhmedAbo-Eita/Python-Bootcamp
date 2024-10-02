# nstruction
# Define a function which takes three integer number as parameters and returns maximum of them.
#
# Input
# max_of_three(4,5,3)
# Output
# 5

#definition of the function
def max_number(num1,num2,num3):
    if num1>num2 and num1>num3:
        return num1
    elif num2>num1 and num2>num3:
        return num2
    else:
        return num3

#Take input from user
number1 = float(input("Enter the first number = "))
number2 = float(input("Enter the second number = "))
number3 = float(input("Enter the third number = "))

#calling the function and print the mak value
print(max_number(number1,number2,number3))