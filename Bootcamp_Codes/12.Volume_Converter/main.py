# Define a function that converts fluid ounces to milliliters and prints the result to the console.
# Take into account that 1 fluid ounce is equal to 29.57353 milliliters.
# Example:
# volume_converter(5)
# Output:
# 147.86765 

def volume_converter(num):
    result = num*29.57353
    print(result)

volume_converter(6)