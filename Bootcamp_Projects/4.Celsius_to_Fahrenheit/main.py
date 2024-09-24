# Celsius to Fahrenheit Project
# Instruction
# Write a program which prompts the user for a Celsius temperature, convert the temperature to Fahrenheit,
# and print out the converted temperature. Formula : (°C × 9/5) + 32 = °F
# Input
# Enter Temperature in Celsius: 10
# Output
# 10 Celsius = 50 Fahrenheit


temp = input("Enter Tempreture in Celsius: ")
tempf = (float(temp)*(9/5))+32
print(f"{temp} Celsius = {tempf} Fahrenheit")