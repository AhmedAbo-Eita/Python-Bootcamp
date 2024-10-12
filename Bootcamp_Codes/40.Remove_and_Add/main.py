# Remove and Add
# Remove an element at index 4 in a given list and add it to the 2nd position and at the end of the list.

# custom_list = [10, 44, 57, 99, 11, 33, 84]
# Output
# [10, 44, 11, 57, 99, 33, 84, 11]

#given list
custom_list = [10, 44, 57, 99, 11, 33, 84]
#remove element at index 4
num = custom_list[4]
custom_list.remove(custom_list[4])
#insert in the index 2
custom_list.insert(2,num)
#insert at the end of list
custom_list.append(num)
#print the list
print(custom_list)