# Square Of Items
# Implement a function that takes a list as a parameter and turn list items into their square.

# Example
# custom_list = [1,2,3,4,5]
# square_list(custom_list)
# Output
# [1,4,9,16,25]

#input list 
custom_list = [1,2,3,4,5]

#function that square the number in list
def square_list(p_list):
    for index in range(0,len(p_list)):
        p_list[index] = p_list[index] ** 2
    return p_list

#calling the function and pass the input list to it
result = square_list(custom_list)

#print the result as list
print(result)