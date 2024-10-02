# nstruction
# Define a function which takes a temperature as a parameter:
# returns Hot if the temperature is greater than 28. returns Warm if the temperature is between 18 and 28, including both. returns Cold if the temperature is less than 18

# Input
# 18

# Output
# Warm


#function definition 
def weather_condition(temp):
    if temp > 28:
        return "Hot"
    elif temp <= 28 and temp >= 18:
        return "Warm"
    elif temp < 18:
        return "Cold"

#take input from user 
tempreture = float(input("Enter the tempreture = "))
print(weather_condition(tempreture))