# Generate Dictionary
# Implement a function which takes integer number (n) as a parameter and returns dictionary with keys from 1 to n
# and values are square of the numbers from 1 to n.
#
# Example
# generate_dictionary(5)
#
# Output
# {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

#function which generate dictionary
def generate_dictionary(num):
    dictionary = {}
    for number in range(1,num+1):
        dictionary[number] = number**2
    return dictionary

#calling the function and pass the value for it and print it
print(generate_dictionary(5))