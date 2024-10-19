# Multiply Dictionary Items
# Implement a function which takes dictionary as a parameter and returns multiplication of values of this dictionary.
#
# Example
#
#     my_dict = {"One" : 1, "Two" : 2, "Three" : 3, "Four" : 4}
#     multiply_values(my_dict)
#
# Output
# 24

#function take the dictionary and multibly the values of its keys
def multiply_values(p_my_dict):
    mul = 1
    for key in p_my_dict:
        mul *= p_my_dict[key]
    return mul

#given dictionary
my_dict = {"One" : 1, "Two" : 2, "Three" : 3, "Four" : 4}

#Calling the function and get the multiplication of its key's values
print(multiply_values(my_dict))