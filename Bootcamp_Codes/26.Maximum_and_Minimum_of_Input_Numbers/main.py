# Write another program that prompts for a list of numbers as we did in previous exercises and at the end prints out both the
# maximum and minimum of the inputted numbers.
#
# For Example
#
#     Enter a number: 1
#     Enter a number: 3
#     Enter a number: 2
#     Enter a number: 4
#     Enter a number: done
#
# Output
#
# Maximum number: 4.0, Minimum number: 1.0

def check_for_float(p_input):
    try:
        val = float(p_input)
        return val
    except (ValueError, TypeError):
        print("Error, please enter numeric input")
        return False

inputs = []
counter = 0
while True:
    input_val = input("Enter a number: ")
    if input_val == "done":
        break
    else:
        inputs.append(check_for_float(input_val))
        counter +=1

#finding the max number
maximum = 0
for num in inputs:
    if num > maximum:
        maximum = num

#finding the minimum number
minimum  = maximum
for num in inputs:
    if num < minimum:
        minimum = num

#print the values of minimum and maximum
print(f"Maximum number: {maximum}, Minimum number: {minimum}")