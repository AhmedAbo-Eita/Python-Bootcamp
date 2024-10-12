# Reverse a List using Slice Operator
# Reverse a given list in using Slice operator.

# Hint : Use step parameter of Slice operator - [start:stop:step]

# custom_list = [1,2,3,4,5,6,7,8,9,10]
# Output
# [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]

#given list
custom_list = [1,2,3,4,5,6,7,8,9,10]

#creating a reverse list
reversed_list = custom_list[-1:-len(custom_list)-1:-1]

#print the output
print(reversed_list)