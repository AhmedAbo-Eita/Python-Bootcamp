# Gross Pay with Ovetime
# Instruction
# Rewrite the Gross Pay Project (Project 3) program to give the employee 1.5 times the hourly rate for hours worked 
# above 40 hours. Here again the program prompts the user for hours and rate per hour to compute gross pay. You need
#  to take into account that the result has exactly two digits after the decimal place.
# Hint: overtime = hour - 40

# Input
# Enter Hours: 45
# Enter Rate: 5
# Output
# Pay: 237.5

hours = float(input("Enter Hours: "))
rate = float(input("Enter Rate: ")) 
pay = 0
if hours>40:
    pay = ((hours-40)*1.5*rate)+(40*rate)
else:
    pay = hours*rate
round(pay,2)
#convert two input to float -- multiply them them print the output
print(f"Pay: {pay}")