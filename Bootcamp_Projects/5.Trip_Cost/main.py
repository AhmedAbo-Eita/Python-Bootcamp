# Trip Cost Calculator Project
# Instruction

# Write a program which calculates trip cost for a user.

#     Create a greeting for your program.
#     Ask the user for number of days.
#     Ask the user for hotel price.
#     Ask the user for flight price.
#     Ask the user for rental car price.
#     Ask for other expenses.
#     Combine all expenses together and print with 2 digits after decimal places.

# Input
# Welcome to the Trip Cost Calculator!
# How many days will you stay? 3
# How much does hotel cost per night? $30
# How much does flight cost? $50
# If you need rental car please enter the price otherwise enter zero. $10
# Enter other possible expenses $0

# Output
# Total Cost: $170.0


#     Create a greeting for your program.
print("Welcome to the Trip Cost Calculator!")

#     Ask the user for number of days.
days = input("How many days will you stay? ")

#     Ask the user for hotel price.
hotel_price = input("How much does hotel cost per night? $")

#     Ask the user for flight price.
flight_price = input("How much does flight cost? $")

#     Ask the user for rental car price.
car_price = input("If you need rental car please enter the price otherwise enter zero. $")

#     Ask for other expenses.
expenses_price = input("Enter other possible expenses $")

#     Combine all expenses together and print with 2 digits after decimal places.
total_cost = (float(days)*(float(hotel_price)+float(car_price)))+float(flight_price)+float(expenses_price)

print("Total Cost: $",round(total_cost,2))



