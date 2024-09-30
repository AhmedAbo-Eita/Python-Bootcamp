# Instruction

# Rewrite Gross Pay with Overtime Project (Project 6) and create a function called compute_pay which takes two parameters (hours and rate).
# Additionally, we need to create another function which checks if the type of "input" is a float or not.
# If the values for hour or rate is not float we will return error.

import GrossPay as gs
#take input from user
try:
    hours_in = float(input("Enter Hours: "))
except:
    print("Error, Enter the hours as numbers")
    quit()
try:
    rate_in = float(input("Enter Rate: "))
except:
    print("Error, Enter the rate as numbers")
    quit()
#calling gros pay function
pay = gs.GrossPay(hours_in,rate_in)
#print the pay
print(f"pay: {pay}")