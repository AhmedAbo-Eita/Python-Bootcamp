# Write a program which repeatedly reads numbers until the user enters "done". Once “done” is entered, print out the total, count, and average of the numbers.
# If the user enters anything other than a number, detect their mistake using try and except and print an error message and skip to the next number.

# Step 1 - Create a function which checks for numbers using try and except block.
# Step 2 - Inside while loop ask for input
# Step 3 - Calculate count, sum and average

#     Enter a number: 2
#     Enter a number: 4
#     Enter a number: six
#     Error, please enter numeric input
#     Enter a number: 6
#     Enter a number: done
#     12.0 3 4.0

inputs = []
counter = 0
while True:
    user_input = input("Enter a number: ")
    if user_input == "done":
        break
    else:
        try:
            inputs.append(float(user_input))
            counter += 1
        except:
            print("Error, please enter numeric input")

sum = 0
for num in inputs:
    sum = sum + num

average = sum / counter

print(sum , counter , average)
