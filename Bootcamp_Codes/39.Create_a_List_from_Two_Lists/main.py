# Create a List from Two Lists
# Given two lists create a third list by picking an odd-index element from the first list
#  and even-index elements from the second.

# list_one = [4, 12, 16, 21, 24, 28, 32]
# list_two = [5, 10, 15, 20, 25, 30, 35]
# Output
# [12, 21, 28, 5, 15, 25, 35]

#given lists
list_one = [4, 12, 16, 21, 24, 28, 32]
list_two = [5, 10, 15, 20, 25, 30, 35]
#New list
list_three = []

for num in range(1,len(list_one),2):
    list_three.append(list_one[num])
    

for num in range(0,len(list_one),2):
    list_three.append(list_two[num])
    

print(list_three)