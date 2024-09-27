# Instructions
# Rewrite Gross Pay program using try and except so that your program handles non-numeric input gracefully by printing a message and exiting the program.

# Example Input
# Enter Hours: 20
# Enter Rate: ten
# Example Output
# Error, please enter numeric input for Rate

# Hint
#The quit() function is used to exit a python program.
#When it encounters the quit() function in the system, it terminates the execution of the program completely.
#It is possible to write programs that handle selected exceptions. In Python, a value is the information that is 
# stored within a certain object. To encounter a ValueError in Python means that is a problem with the content of the object you
#  tried to assign the value to.

try:
    hours = float(input("Enter Hours: "))
except ValueError:
    print("Error, please enter numeric input for Hours")
    quit()

try: 
    rate = float(input("Enter Rate: ")) 
except ValueError:
    print("Error, please enter numeric input for Rate")
    quit()

pay = 0
if hours>40:
    pay = ((hours-40)*1.5*rate)+(40*rate)
else:
    pay = hours*rate
round(pay,2)
#convert two input to float -- multiply them them print the output
print(f"Pay: {pay}")