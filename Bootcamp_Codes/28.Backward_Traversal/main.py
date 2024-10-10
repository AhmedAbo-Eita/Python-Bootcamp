# Write a while loop that starts at the last character in the string and works its way backwards to 
# the first character in the string, printing each letter on a separate line, except backwards.

# Input
# Enter a string: Python
# Output
#     n
#     o
#     h
#     t
#     y
#     P

user_input = input("Enter a string: ")

index = len(user_input)-1
while index >=0:
    output = user_input[index]
    print(output)
    index -=1 