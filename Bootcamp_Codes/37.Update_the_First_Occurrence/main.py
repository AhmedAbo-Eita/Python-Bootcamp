# Update the First Occurrence
# Find the value of 50 in a given list, and if it is present, replace  the first occurrence of a value with 5.

# For example
# list1 = [10, 10, 5, 15, 50, 50, 20]
# Output
# [10, 10, 5, 15, 5, 50, 20]

#given list 
list1 = [10, 10, 5, 15, 50, 50, 20]
#finding the index of first 50
index_of_50 = list1.index(50)
#remove 50 from list
list1.remove(50)
# add 5 in the list in the same index of 50
list1.insert(index_of_50,5)
#print the updated list
print(list1)