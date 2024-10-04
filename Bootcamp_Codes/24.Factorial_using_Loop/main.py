# Implement a function that takes an integer number as a parameter and returns factorial of this number.
#
# Factorial Equation (!)
# 5! = 5 x 4 x 3 x 2 x 1 = 120
# 4! = 4 x 3 x 2 x 1 = 24

# If input is 0 then the return value will be: The factorial of 0 is 1
# if input is a negative number then the return value will be: Factorial does not exist for negative numbers

# Example
#     factorial(4) # The factorial of 4 is 24
#     factorial(-1)  # Factorial does not exist for negative numbers

def factorial(p_num):
    result = 1
    num = p_num
    if p_num>0:
        while p_num != 0:
            result = result * p_num
            p_num -= 1
        return f"The factorial of {num} is {result}"
    elif p_num == 0:
        return "The factorial of 0 is 1"
    else:
        return "Factorial does not exist for negative numbers"

print(factorial(5))