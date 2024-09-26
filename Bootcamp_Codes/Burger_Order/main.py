# Burger Order
# Write a program that calculates final bill Burger Order Price based on a user's choice.
# Price List.
# Mini Burger (M) : $5
# Normal Burger (N): $8
# Large Burger (L) : $10
# Add Mushroom : For Mini and Normal = $1, For Large = $2
# Extra Cheese : $1

# Example Input
#     size = "N"
#     add_mushroom = "Y"
#     extra_cheese = "N"
# Example Output
#     Your final bill is: $9.

# TODO
print("Welcome to Burger Shop!")
cost = 0
size = input("What size Burger do you want? M, N or L ")
if size=='M':
    cost+=5
if size=='N':
    cost+=8
if size=='L':
    cost+=10
    
mushroom = input("Do you want mushroom? Y or N ")
if(size == 'M' or size == 'N') and mushroom=='Y':
    cost+=1
if(size == 'L' and mushroom=='Y'):
    cost+=2

ExtraCheese = input("Do you want extra cheese? Y or N ")
if ExtraCheese == 'Y':
    cost+=1

print(f"Your final bill is: ${cost}")