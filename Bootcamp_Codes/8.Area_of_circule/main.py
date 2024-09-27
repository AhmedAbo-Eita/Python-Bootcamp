# Area of Circle
# Write a program that calculates the area of circle based on user input of radius using equation provided below. 
# The output must be rounded to 2 decimal places.
# Example Input
# Enter Radius: 4
# Example Output
# The area of circle is: 50.27



import math
radius = float(input("Enter Radius: "))
area = round(math.pi * pow(radius,2),2)
print(f"The area of circle is: {area}")