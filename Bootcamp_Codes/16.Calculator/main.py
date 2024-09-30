# Implement code block which asks two numbers and operation (+,-,*,/) that we want to perform on these numbers and returns the result.

# For example
#     What is the first number? 2
#     What is the second number? 4
#     Pick operation from this list (+,-,*,/) *
#
# Output
#     2 * 4 = 8


#functions definitions
def add(num1,num2):
    """This function Add 2 Numbers and return the result"""
    return num1+num2

def subtract(num1,num2):
    """This function subtract 2 Numbers and return the result"""
    return num1-num2

def multiplication(num1,num2):
    """This function multiply 2 Numbers and return the result"""
    return num1*num2

def division(num1,num2):
    """This function divide 2 Numbers and return the result"""
    return num1/num2

#Take input from user
first_number = float(input("What is the first number? "))
second_number = float(input("What is the second number? "))
operator = input("Pick operation from this list (+,-,*,/) ")

#code logic
if operator == '+':
    result = add(first_number,second_number)
elif operator == '-':
    result = subtract(first_number,second_number)
elif operator == '*':
    result = multiplication(first_number,second_number)
elif operator == '/':
    result = division(first_number,second_number)
else:
    print("Error - Enter correct operator")

print(f"{first_number} {operator} {second_number} = {result}")


